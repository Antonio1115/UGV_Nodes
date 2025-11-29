import time
import math
from ugv_logger.ugv_logger_node import UGVLogger

def fake_sensor_stream(num_samples=50):
    """
    Simulates UGV + UAV motion for testing.
    UGV moves straight, UAV ascends & circles.
    """

    for i in range(num_samples):
        t = time.time()

        # Simulated UGV motion (straight line)
        ugv_x = 1.0 + 0.1 * i
        ugv_y = 2.0
        ugv_heading = 0.0

        # Simulated UAV motion (circle in XY plane + increasing altitude)
        r = 5
        angle = i * 0.1
        uav_x = r * math.cos(angle)
        uav_y = r * math.sin(angle)
        uav_z = 2.0 + 0.05 * i

        yield {
            "timestamp": t,
            "ugv_pos": (ugv_x, ugv_y, ugv_heading),
            "uav_pos": (uav_x, uav_y, uav_z)
        }

        time.sleep(0.05)  # 50ms delay for realism


def main():
    print("▶ Creating logger...")
    logger = UGVLogger()

    print("▶ Streaming fake sensor data into logger...")
    for entry in fake_sensor_stream():
        logger.write_log(entry)

    print("\n✔ Finished! Log files saved in /logs/")


if __name__ == "__main__":
    main()
