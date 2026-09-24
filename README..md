# Python System monotoring tool

A lightweight Python-based **system-monotoring-tool** that checks the current health of CPU, RAM, and disk usage of a system.

The tool generates a timestamped health report, displays the results in the terminal, identifies high resource usage, and saves the report to a local log file.

## Features

- Monitor CPU usage
- Monitor RAM usage
- Monitor Disk usage
- Display resource usage in percentage
- Show warnings when usage reaches the configured threshold
- Generate timestamped server health reports
- Save reports automatically to `system_health.log`
- Supports Windows and Linux system drive detection
- Lightweight and easy to run from the command line

## Technologies Used

- Python
- psutil
- datetime
- pathlib
- os

## Project Structure

```text
SystemMonitoringTool/
│
├── main.py
├── system_health.log
└── README.md
```

> `system_health.log` is created automatically after the program runs.

## Requirements

- Python 3.x
- psutil

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd SystemMonitoringTool
```

### 2. Install the required dependency

```bash
pip install psutil
```

## How to Run

```bash
python main.py
```

The program collects the current CPU, RAM, and disk usage and displays a health report in the terminal.

Example:

```text
Server Health Report - 2026-09-24 17:00:00 IST
CPU Usage: 35.2% - OK: CPU usage is normal.
RAM Usage: 62.4% - OK: RAM usage is normal.
Disk Usage: 71.5% - OK: Disk usage is normal.

Report saved to: server_health.log
```

## Monitoring Threshold

The project uses an **80% warning threshold** for CPU, RAM, and disk usage.

```python
CPU_WARNING_THRESHOLD = 80
MEMORY_WARNING_THRESHOLD = 80
DISK_WARNING_THRESHOLD = 80
```

If a resource reaches or exceeds the threshold, the tool reports:

```text
WARNING: CPU usage is high!
```

Otherwise:

```text
OK: CPU usage is normal.
```

## How It Works

### CPU Monitoring

CPU usage is measured over a one-second interval using `psutil`.

### RAM Monitoring

The tool obtains the current RAM utilization percentage using `psutil.virtual_memory()`.

### Disk Monitoring

The main system drive is monitored.

- On Windows, the `SystemDrive` environment variable is used.
- On Linux, the root directory `/` is monitored.

### Health Status

Each metric is compared with its configured warning threshold.

```text
Usage >= Threshold
        ↓
     WARNING

Usage < Threshold
        ↓
       OK
```

## Log File

After each execution, the generated health report is appended to:

```text
system_health.log
```

The log contains the timestamp, CPU usage, RAM usage, disk usage, and corresponding health status.

## Main Functions

| Function | Purpose |
|---|---|
| `get_cpu_usage()` | Gets CPU usage percentage |
| `get_memory_usage()` | Gets RAM usage percentage |
| `get_disk_usage()` | Gets disk usage percentage |
| `check_status()` | Checks whether resource usage is normal or high |
| `collect_health_report()` | Collects metrics and creates the report |
| `save_report()` | Saves the report to the log file |
| `main()` | Runs the monitoring process |

## Project Workflow

```text
Start
  │
  ▼
Collect CPU Usage
  │
  ▼
Collect RAM Usage
  │
  ▼
Collect Disk Usage
  │
  ▼
Compare With 80% Threshold
  │
  ▼
Generate Health Report
  │
  ├──────────────► Display Report
  │
  └──────────────► Save Report
                         │
                         ▼
                 system_health.log
```

## Use Cases

This tool can be used for:

- Basic system health checking
- System resource monitoring
- Learning Python system administration
- Understanding the `psutil` library
- Creating a foundation for a larger monitoring system

## Limitations

The current version is a lightweight command-line monitoring tool. It performs a health check when the program is executed and does not currently provide:

- A graphical user interface
- A web dashboard
- Continuous background monitoring
- Email/SMS notifications
- Historical graphs
- Process-level monitoring

## Future Enhancements

Possible improvements include:

- Real-time continuous monitoring
- GUI dashboard using Tkinter
- Web dashboard using Flask
- CPU/RAM/Disk usage graphs
- Process monitoring
- Email notifications for high usage
- Configurable warning thresholds
- Database-based historical monitoring
- Automatic scheduled health checks

## License

This project is intended for educational and development purposes.

## Author

**Jasleen Kaur**

GitHub: [jasleenkaur707](https://github.com/jasleenkaur707)
