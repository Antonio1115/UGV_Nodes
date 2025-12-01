# mission_manager.py

import time
import threading


class MissionState:
    """Simple enumeration of mission states."""
    INIT = "INIT"
    IDLE = "IDLE"
    PREPARE = "PREPARE"
    EXECUTE = "EXECUTE"
    PAUSED = "PAUSED"
    ERROR = "ERROR"
    COMPLETE = "COMPLETE"


class MissionManager:
    """
    Mission Manager for UGV/UAV challenges.
    Accepts control flags (strings) and updates mission state.
    Outputs the current mission state.
    """

    def __init__(self):
        self.state = MissionState.INIT
        self.current_mission = None  # e.g., "challenge_1", "challenge_2"

        print("[MissionManager] Initialized in INIT state")

        # Start standalone loop
        self._running = True
        threading.Thread(target=self._loop, daemon=True).start()

    # Standalone loop that periodically prints state
    def _loop(self):
        while self._running:
            print(f"[MissionManager] Current State: {self.state}")
            time.sleep(1)

    # Public API: Handle external commands
    def handle_control_flag(self, flag: str):
        """
        Process incoming string control flags.
        Examples:
            "START", "STOP", "PAUSE", "RESUME", "ERROR", "COMPLETE"
        """

        flag = flag.upper().strip()
        print(f"[MissionManager] Received control flag: {flag}")

        if flag == "START":
            self._handle_start()

        elif flag == "STOP":
            self._handle_stop()

        elif flag == "PAUSE":
            self._handle_pause()

        elif flag == "RESUME":
            self._handle_resume()

        elif flag == "ERROR":
            self._handle_error()

        elif flag == "COMPLETE":
            self._handle_complete()

        else:
            print(f"[MissionManager] WARNING: Unknown control flag '{flag}'")

    # Internal handlers for each flag
    def _handle_start(self):
        if self.state in (MissionState.IDLE, MissionState.INIT):
            print("[MissionManager] Preparing mission...")
            self.state = MissionState.PREPARE
        else:
            print("[MissionManager] START ignored (wrong state)")

    def _handle_stop(self):
        print("[MissionManager] Stopping mission...")
        self.state = MissionState.IDLE
        self.current_mission = None

    def _handle_pause(self):
        if self.state == MissionState.EXECUTE:
            print("[MissionManager] Pausing mission...")
            self.state = MissionState.PAUSED
        else:
            print("[MissionManager] PAUSE ignored (wrong state)")

    def _handle_resume(self):
        if self.state == MissionState.PAUSED:
            print("[MissionManager] Resuming mission...")
            self.state = MissionState.EXECUTE
        else:
            print("[MissionManager] RESUME ignored (wrong state)")

    def _handle_error(self):
        print("[MissionManager] ERROR triggered")
        self.state = MissionState.ERROR

    def _handle_complete(self):
        if self.state == MissionState.EXECUTE:
            print("[MissionManager] Mission complete")
            self.state = MissionState.COMPLETE
        else:
            print("[MissionManager] COMPLETE ignored (wrong state)")

    # Output API
    def get_state(self):
        """Returns current mission state."""
        return self.state

    # Shutdown
    def stop(self):
        self._running = False
        print("[MissionManager] Shutting down")
