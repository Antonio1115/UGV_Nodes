# **ugv_nodes**

This repository contains the first versions of the SMU Drone Club’s UGV nodes. The goal right now is to build and test the **core logic** of each node without depending on ROS2.

---

## 🚧 **Current Status**

### Python modules

You currently have two working modules:

* **UGV Logger**

  * Logs timestamps + UGV/UAV positions to CSV/JSONL
  * Testable with dummy data
  * No ROS2 dependencies

* **Mission Manager**

  * Simple mission state machine
  * Accepts string-based control flags (`"START"`, `"STOP"`, `"PAUSE"`, etc.)
  * Outputs the current mission state
  * Runs in standalone mode for now

### ✔ `examples/` folder

You have example scripts that let you test the modules with:

```
python3 examples/test_logger.py
python3 examples/test_mission_manager.py
```

### ✔ Clean repo layout

The repository uses simple Python packages instead of ROS2 packages, since ROS2 installation on this machine is currently failing.

---

## 📁 **Repository Structure**

```
ugv_nodes/
│
├── mission_manager/
│   ├── __init__.py
│   └── mission_manager.py
│
├── ugv_logger/
│   ├── __init__.py
│   └── logger.py
│
└── examples/
    ├── test_logger.py
    └── test_mission_manager.py
```

---

## 🎯 **Next Steps**

* Add challenge-specific logic for Mission Manager
* Integrate UGVLogger with Mission Manager (log mission state transitions)
* Reintroduce ROS2 packaging once Jetsons & ROS environment are available
* Convert modules into ROS2 nodes using rclpy

---
