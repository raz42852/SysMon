from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.layout import Layout
import time
import src.collector
from src.logger import Logger
import sys

class Display:
    def __init__(self, interval, cpu_warn, mem_warn, logger_file):
        self.console = Console()
        self.layout = Layout()
        self.layout.split_column(
            Layout(name="upper"),
            Layout(name="lower")
        )
        self.layout["lower"].split_row(
            Layout(name="left"),
            Layout(name="right"),
        )
        self.panel = Panel("System Monitoring CLI Tool", title="Welcome")
        self.interval = interval
        self.cpu_warn = cpu_warn
        self.mem_warn = mem_warn
        self.logger_file = logger_file
        logger = Logger(self.logger_file)
        with Live(self.layout, refresh_per_second=1) as self.live:
            while True:
                cpu_data = src.collector.getCPUData()
                memory_data = src.collector.getMemory()
                disk_usage_data = src.collector.getDiskUsage()
                self.cpu_table = self.get_cpu_table(cpu_data)
                self.memory_table = self.get_memory_table(memory_data)
                self.disk_usage_table = self.get_disk_usage_table(disk_usage_data)
                logger.save_json(cpu_data, memory_data, disk_usage_data)

                self.layout["upper"].update(self.cpu_table)
                self.layout["left"].update(self.memory_table)
                self.layout["right"].update(self.disk_usage_table)

                try:
                    time.sleep(interval)
                except KeyboardInterrupt:
                    logger.empty_file()
                    self.live.stop()
                    self.console.print("exit program and flush the log :)")
                    sys.exit(0)
                    
    def get_cpu_table(self, cpu_data):
        cpu_table = Table(title="CPU Panel")
        self.layout["upper"].size = 10

        cpu_table.add_column("Num Cores")
        cpu_table.add_column("Num Threads")
        cpu_table.add_column("CPU Percentage")
        cpu_row = [str(cpu_data['cores']),
                    str(cpu_data['threads'])]
        
        if (int(cpu_data['cpu_per']) >= int(self.cpu_warn)):
            cpu_row.append(f"[red]{str(cpu_data['cpu_per'])}%[/red]")
        else:
            cpu_row.append(f"{str(cpu_data['cpu_per'])}%")
        
        for i in range(len(cpu_data['cpu_per_per'])):
            cpu_table.add_column(f"Thread {i+1}")
            cpu_row.append(f"{cpu_data['cpu_per_per'][i]}%")
            
        for i in range(len(cpu_data['freq'])):
            cpu_table.add_column(f"Frequency Thread {i+1}")
            cpu_row.append(str(cpu_data['freq'][i].current))

        cpu_table.add_row(*cpu_row)
        for i in range(len(cpu_row)):
            if "[" in cpu_row[i]:
                cpu_row[i] = cpu_row[i][cpu_row[i].find("]") + 1:cpu_row[i].find("[", 1):]
        return cpu_table

    def get_memory_table(self, memory_data):
        memory_table = Table(title="Memory Panel")
        memory_table.add_column("Total")
        memory_table.add_column("Available")
        memory_table.add_column("Used")
        memory_table.add_column("Percent")
        memory_table.add_column("Free")
        memory_data[3] = f"[red]{memory_data[3]}%[/red]" if (int(memory_data[3]) >= int(self.mem_warn)) else f"{memory_data[3]}%"
        memory_table.add_row(*memory_data)
        for i in range(len(memory_data)):
            if "[" in memory_data[i]:
                memory_data[i] = memory_data[i][memory_data[i].find("]") + 1:memory_data[i].find("[", 1):]
        return memory_table

    def get_disk_usage_table(self, disk_usage_data):
        disk_usage_table = Table(title="Disk Usage Panel")
        disk_usage_table.add_column("Device")
        disk_usage_table.add_column("Total")
        disk_usage_table.add_column("Used")
        disk_usage_table.add_column("Free")
        disk_usage_table.add_column("Use")
        disk_usage_table.add_column("Type")
        disk_usage_table.add_column("Mount")
        for row in disk_usage_data:
            disk_usage_table.add_row(*row)
        return disk_usage_table