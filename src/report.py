import json

class Report:
    def __init__(self, path, date, logger):
        self.path = path
        self.date = date
        self.logger = logger
        self.report = self.get_daily_report()

    def get_daily_report(self):
        logger_index = self.logger.logger_day_index(self.date)
        if (logger_index != -1):
            with open(self.path, 'r') as file:
                file_data = json.load(file)
                day = file_data[logger_index]
                threshold_cpu = self.get_cpu_report(day["CPU"])
                threshold_memory = self.get_memory_report(day["Memory"])
                threshold_disk_usage = self.get_disk_usage_report(day["Disk Usage"])
                data = {
                    "CPU" : threshold_cpu,
                    "Memory" : threshold_memory,
                    "Disk Usage" : threshold_disk_usage
                }
                return data
        else:
            return None
        
    def get_cpu_report(self, cpu_data):
        threshold_data  = {}
        if (list(cpu_data)):
            for title, value in cpu_data[0].items():
                try:
                    threshold_data[title] = {
                        "Minimum" : float((str(value))[:len(str(value))-1]),
                        "Avg" : 0,
                        "Maximum" : 0
                    }
                except ValueError:
                    threshold_data[title] = value
            threshold_data.pop("Num Cores")
            threshold_data.pop("Num Threads")
            for row in cpu_data:
                for title, value in row.items():
                    if (title == "Num Cores" or title == "Num Threads"):
                        continue
                    val_num = float((str(value))[:len(str(value))-1])
                    if threshold_data[title]["Minimum"] > val_num:
                        threshold_data[title]["Minimum"] = val_num
                    threshold_data[title]["Avg"] += val_num
                    if threshold_data[title]["Maximum"] < val_num:
                        threshold_data[title]["Maximum"] = val_num
            for title, value in threshold_data.items():
                threshold_data[title]["Avg"] = threshold_data[title]["Avg"] / len(cpu_data)
        return threshold_data

    def get_memory_report(self, memory_data):
        threshold_data  = {}
        if (list(memory_data)):
            for title, value in memory_data[0].items():
                try:
                    threshold_data[title] = {
                        "Minimum" : float((str(value))[:len(str(value))-1]),
                        "Avg" : 0,
                        "Maximum" : 0
                    }
                except ValueError:
                    threshold_data[title] = value
            threshold_data.pop("Total")
            for row in memory_data:
                for title, value in row.items():
                    if (title == "Total"):
                        continue
                    val_num = float((str(value))[:len(str(value))-1])
                    if threshold_data[title]["Minimum"] > val_num:
                        threshold_data[title]["Minimum"] = val_num
                    threshold_data[title]["Avg"] += val_num
                    if threshold_data[title]["Maximum"] < val_num:
                        threshold_data[title]["Maximum"] = val_num
            for title, value in threshold_data.items():
                threshold_data[title]["Avg"] = threshold_data[title]["Avg"] / len(memory_data)
        return threshold_data

    def get_disk_usage_report(self, disk_usage_data):
        threshold_data  = {}
        if (list(disk_usage_data)):
            for disk in disk_usage_data[0]:
                threshold_data[disk['Device']] = {}
                for title, value in disk.items():
                    try:
                        threshold_data[disk['Device']][title] = {
                            "Minimum" : float((str(value))[:len(str(value))-1]),
                            "Avg" : 0,
                            "Maximum" : 0
                        }
                    except ValueError:
                        threshold_data[disk['Device']][title] = value
            for disk in disk_usage_data[0]: 
                threshold_data[disk['Device']].pop("Device")
                threshold_data[disk['Device']].pop("Total")
                threshold_data[disk['Device']].pop("Type")
                threshold_data[disk['Device']].pop("Mount")
            for row in disk_usage_data: 
                for disk in row:
                    for title, value in disk.items():
                        if (title == "Device" or title == "Total" or title == "Type" or title == "Mount"):
                            continue
                        val_num = float((str(value))[:len(str(value))-1])
                        if threshold_data[disk['Device']][title]["Minimum"] > val_num:
                            threshold_data[disk['Device']][title]["Minimum"] = val_num
                        threshold_data[disk['Device']][title]["Avg"] += val_num
                        if threshold_data[disk['Device']][title]["Maximum"] < val_num:
                            threshold_data[disk['Device']][title]["Maximum"] = val_num
            for device, disk in threshold_data.items():
                for title, value in disk.items():
                    threshold_data[device][title]["Avg"] = threshold_data[device][title]["Avg"] / len(disk_usage_data)
        return threshold_data