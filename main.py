from monitor.system_stats import get_system_stats
from monitor.process_stats import get_top_processes

def main():
    stats = get_system_stats()
    processes = get_top_processes()

    print("=== System Monitor ===")
    print(f"CPU:    {stats['cpu_percent']}%")
    print(f"Memory: {stats['memory_used_gb']} / {stats['memory_total_gb']} GB ({stats['memory_percent']}%)")
    print(f"Disk:   {stats['disk_used_gb']} / {stats['disk_total_gb']} GB ({stats['disk_percent']}%)")

    print("\nTop Processes:")
    print(f"{'PID':<8}{'NAME':<20}{'CPU%'}")

    for p in processes:
        print(f"{p['pid']:<8}{p['name']:<20}{p['cpu_percent']}")

if __name__ == "__main__":
    main()
