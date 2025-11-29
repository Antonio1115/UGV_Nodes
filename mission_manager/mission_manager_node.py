import time
import threading


class MissionManager:
    """
    Minimal mission manager template.
    Runs a simple 1 Hz loop and keeps track of the current mission.
    """

    def __init__(self):
        self.current_mission = "idle"
        self._stop_flag = False

        # Background loop (1 Hz)
        threading.Thread(
            target=self._loop,
            daemon=True
        ).start()


    def _loop(self):
        while not self._stop_flag:
            self.update()
            time.sleep(1.0)


    def update(self):
        """Main loop logic placeholder (executed every second)."""
        print(f"[MissionManager] Current mission: {self.current_mission}")


    def set_mission(self, mission_name: str):
        print(f"[MissionManager] Switching mission to: {mission_name}")
        self.current_mission = mission_name


    def stop(self):
        self._stop_flag = True


# Standalone test runner
if __name__ == "__main__":
    manager = MissionManager()
    manager.set_mission("takeoff_and_land")

    print("Mission Manager running… press CTRL+C to exit.")
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        manager.stop()
