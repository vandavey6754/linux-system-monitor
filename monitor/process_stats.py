import time
import psutil

def get_top_processes(limit=5, sample_seconds=0.2):
    """
    Return top processes by CPU%.
    On macOS, cpu_percent may be None until it's "primed", so we sample twice.
    """
    # Prime CPU percent counters
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    time.sleep(sample_seconds)

    processes = []
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            cpu = proc.cpu_percent(None)
            processes.append({
                "pid": proc.pid,
                "name": proc.info.get("name") or "unknown",
                "cpu_percent": cpu,
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(key=lambda p: p["cpu_percent"], reverse=True)
    return processes[:limit]
