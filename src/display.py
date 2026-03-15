from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.layout import Layout
from rich import print
import time
import collector

panel = Panel("System Monitoring CLI Tool", title="Welcome")
print(panel)

console = Console()
layout = Layout()

layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)
layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)

# Use Live to update the layout
with Live(layout, refresh_per_second=1) as live:
    while True:
        cpu_data = collector.getCPUData()
        cpu_table = Table(title="CPU Panel")

        cpu_table.add_column("Num Cores")
        cpu_table.add_column("Num Threads")
        cpu_table.add_column("CPU Percentage")
        cpu_row = [str(cpu_data['cores']),
                   str(cpu_data['threads']),
                   f"{str(cpu_data['cpu_per'])}%"]
        
        for i in range(len(cpu_data['cpu_per_per'])):
            cpu_table.add_column(f"Thread {i+1}")
            cpu_row.append(f"{cpu_data['cpu_per_per'][i]}%")
        
        for i in range(len(cpu_data['freq'])):
            cpu_table.add_column(f"Frequency Thread {i+1}")
            cpu_row.append(str(cpu_data['freq'][i].current))

        cpu_table.add_row(*cpu_row)

        memory_table = Table(title="Memory Panel")
        memory_table.add_column("Total")
        memory_table.add_column("Available")
        memory_table.add_column("Used")
        memory_table.add_column("Percent")
        memory_table.add_column("Free")
        memory_data = collector.getMemory()

        memory_table.add_row(*memory_data)

        disk_usage_table = Table(title="Disk Usage Panel")
        disk_usage_table.add_column("Device")
        disk_usage_table.add_column("Total")
        disk_usage_table.add_column("Used")
        disk_usage_table.add_column("Free")
        disk_usage_table.add_column("Use")
        disk_usage_table.add_column("Type")
        disk_usage_table.add_column("Mount")
        disk_usage_data = collector.getDiskUsage()
        for row in disk_usage_data:
            disk_usage_table.add_row(*row)
        # ... populate with data from collector ...

        layout["upper"].update(cpu_table)
        layout["left"].update(memory_table)
        layout["right"].update(disk_usage_table)

        time.sleep(2)