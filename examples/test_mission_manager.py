from mission_manager.mission_manager import MissionManager
import time

mgr = MissionManager()

time.sleep(2)
mgr.handle_control_flag("START")

time.sleep(2)
mgr.handle_control_flag("PAUSE")

time.sleep(2)
mgr.handle_control_flag("RESUME")

time.sleep(2)
mgr.handle_control_flag("COMPLETE")

time.sleep(2)
mgr.handle_control_flag("STOP")

time.sleep(2)
mgr.stop()
