"""
Python System Health Monitoring 
Monitors CPU, memory (RAM), and disk usage, prints health warnings,
and saves a timestamped report to system_health.log.

Install dependency:
    pip install psutil

Run:
    python main.py
"""

from datetime import datetime
from pathlib import Path
import os

import psutil


CPU_WARNING_THRESHOLD = 80
MEMORY_WARNING_THRESHOLD = 80
DISK_WARNING_THRESHOLD = 80
LOG_FILE = Path(__file__).with_name("system_health.log")


def get_cpu_usage():
    """Return CPU usage percentage measured over one second."""
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    """Return RAM usage percentage."""
    return psutil.virtual_memory().percent


def get_disk_usage():
    """Return disk usage percentage for the main system drive."""
    system_drive = os.environ.get("SystemDrive", "C:") if os.name == "nt" else "/"
    return psutil.disk_usage(system_drive).percent


def check_status(metric_name, usage, threshold):
    """Return a readable status for a metric."""
    if usage >= threshold:
        return f"WARNING: {metric_name} usage is high!"
    return f"OK: {metric_name} usage is normal."


def collect_health_report():
    """Collect system metrics and format a report."""
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()

    lines = [
        f"System Health Report - {timestamp}",
        f"CPU Usage: {cpu:.1f}% - {check_status('CPU', cpu, CPU_WARNING_THRESHOLD)}",
        f"RAM Usage: {memory:.1f}% - {check_status('RAM', memory, MEMORY_WARNING_THRESHOLD)}",
        f"Disk Usage: {disk:.1f}% - {check_status('Disk', disk, DISK_WARNING_THRESHOLD)}",
    ]
    return "\n".join(lines)


def save_report(report):
    """Append the report to the local log file."""
    with LOG_FILE.open("a", encoding="utf-8") as log:
        log.write(report + "\n" + ("-" * 55) + "\n")


def main():
    report = collect_health_report()
    print(report)
    save_report(report)
    print(f"\nReport saved to: {LOG_FILE}")


if __name__ == "__main__":
    main()
