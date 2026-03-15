from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich import print
import time
import collector

panel = Panel("System Monitoring CLI Tool", title="Welcome")
print(panel)

with Live(refresh_per_second=1) as live:
    while True:
        table = Table(title="CPU Panel")
        table.add_column("Num Cores")
        table.add_column("Num Threads")
        cpu_data = collector.getCPUData()
        for i in range(len(cpu_data['cpu_per'])):
            table.add_column(f"Thread {i+1}")
        for i in range(len(cpu_data['freq'])):
            table.add_column(f"Frequency Thread {i+1}")

        # ... populate with data from collector ...

        live.update(table)
        time.sleep(2)