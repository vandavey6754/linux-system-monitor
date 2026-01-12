from monitor.system_stats import get_system_stats

def main():
    stats = get_system_stats()

    print("=== System Monitor ===")
    print(f"CPU:    {stats['cpu_percent']}%")
    print(f"Memory: {stats['memory_used_gb']} / {stats['memory_total_gb']} GB ({stats['memory_percent']}%)")
    print(f"Disk:   {stats['disk_used_gb']} / {stats['disk_total_gb']} GB ({stats['disk_percent']}%)")

if __name__ == "__main__":
    main()
