import json
import csv
import os
import time
from typing import Dict, Any


class UGVLogger:
    """
    Simple logger for storing UGV/UAV position data.
    Writes to both JSONL (one JSON object per line)
    and a CSV file for easy analysis.
    """

    def __init__(self, log_dir: str = "logs"):
        # Create the directory if it doesn't exist
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

        # Use a timestamp to name log files
        timestamp = time.strftime("%Y%m%d_%H%M%S")

        self.jsonl_path = os.path.join(self.log_dir, f"log_{timestamp}.jsonl")
        self.csv_path = os.path.join(self.log_dir, f"log_{timestamp}.csv")

        # Set up the CSV file with headers
        self._init_csv()

    
    def _init_csv(self):
        """Create a new CSV file and write the header row."""
        headers = [
            "timestamp",
            "ugv_x", "ugv_y", "ugv_heading",
            "uav_x", "uav_y", "uav_z"
        ]

        with open(self.csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)


    @staticmethod
    def _validate_data(data: Dict[str, Any]):
        """
        Ensure the dictionary contains the keys and values
        we need to log positions.
        """

        if "timestamp" not in data:
            raise ValueError("Missing required field: 'timestamp'")

        if "ugv_pos" not in data or not isinstance(data["ugv_pos"], (list, tuple)) or len(data["ugv_pos"]) != 3:
            raise ValueError("Expected 'ugv_pos' to be a tuple/list of (x, y, heading)")

        if "uav_pos" not in data or not isinstance(data["uav_pos"], (list, tuple)) or len(data["uav_pos"]) != 3:
            raise ValueError("Expected 'uav_pos' to be a tuple/list of (x, y, z)")


    def write_log(self, data: Dict[str, Any]):
        """
        Log one entry to both JSONL and CSV.
        Data dict must contain:
            - timestamp
            - ugv_pos: (x, y, heading)
            - uav_pos: (x, y, z)
        """

        self._validate_data(data)

        # Write JSONL
        with open(self.jsonl_path, "a") as f:
            f.write(json.dumps(data) + "\n")

        # Write CSV
        ugv_x, ugv_y, ugv_h = data["ugv_pos"]
        uav_x, uav_y, uav_z = data["uav_pos"]

        with open(self.csv_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                data["timestamp"],
                ugv_x, ugv_y, ugv_h,
                uav_x, uav_y, uav_z
            ])
