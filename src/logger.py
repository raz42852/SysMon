import json
import datetime 

class Logger:
    def __init__(self, path):
        self.path = path

    def save_json(self, cpu_data, memory_data, disk_usage_data):
        with open(self.path, 'r+') as file:
            file_data = json.load(file)
            logger_index = self.logger_day_index(datetime.date.today().strftime("%d/%m/%Y"))
            file_data[logger_index]["CPU"].append(self.get_cpu_json(cpu_data))
            file_data[logger_index]["Memory"].append(self.get_memory_json(memory_data))
            file_data[logger_index]["Disk Usage"].append(self.get_disk_usage_json(disk_usage_data))
            file.seek(0)
            json.dump(file_data, file)
            file.truncate()

    def get_cpu_json(self, cpu_data):
        dic_cpu = {}
        dic_cpu['Num Cores'] = cpu_data['cores']
        dic_cpu['Num Threads'] = cpu_data['threads']
        dic_cpu['CPU Percentage'] = f"{str(cpu_data['cpu_per'])}%"
        for i in range(len(cpu_data['cpu_per_per'])):
            dic_cpu[f"Thread {i+1}"] = f"{cpu_data['cpu_per_per'][i]}%"
        for i in range(len(cpu_data['freq'])):
            dic_cpu[f"Frequency Thread {i+1}"] = cpu_data['freq'][i].current
        return dic_cpu

    def get_memory_json(self, memory_data):
        dic_memory = {}
        dic_memory['Total'] = memory_data[0]
        dic_memory['Available'] = memory_data[1]
        dic_memory['Used'] = memory_data[2]
        dic_memory['Percent'] = memory_data[3]
        dic_memory['Free'] = memory_data[4]
        return dic_memory

    def get_disk_usage_json(self, disk_usage_data):
        all_disks = []
        for disk in disk_usage_data:
            dic_disk = {}
            dic_disk['Device'] = disk[0]
            dic_disk['Total'] = disk[1]
            dic_disk['Used'] = disk[2]
            dic_disk['Free'] = disk[3]
            dic_disk['Use'] = disk[4]
            dic_disk['Type'] = disk[5]
            dic_disk['Mount'] = disk[6]
            all_disks.append(dic_disk)
        return all_disks

    def init_file(self):
        data = {
            "Date": datetime.date.today().strftime("%d/%m/%Y"),
            "CPU": [],
            "Memory": [],
            "Disk Usage": []
        }
        if (not self.path.exists()):
            open("logger.json", "x")
            self.empty_file(self.path)
        else:
            with open(self.path, 'r+') as file:
                first_char = file.read(1)
                if not first_char:
                    self.empty_file(self.path)
                else :
                    logger_index = self.logger_day_index(datetime.date.today().strftime("%d/%m/%Y"))
                    if logger_index == -1:
                        with open(self.path, 'r+') as file:
                            file_data = json.load(file)
                            file_data.append(data)
                            file.seek(0)
                            json.dump(file_data, file)
                            file.truncate()

    def empty_file(self):
        logger_index = self.logger_day_index(datetime.date.today().strftime("%d/%m/%Y"))
        if not logger_index == -1:
            data = {
                "Date": datetime.date.today().strftime("%d/%m/%Y"),
                "CPU": [],
                "Memory": [],
                "Disk Usage": []
            }
            with open(self.path, 'r+') as file:
                file_data = json.load(file)
                file_data[logger_index] = data
                file.seek(0)
                json.dump(file_data, file)
                file.truncate()

    def logger_day_index(self, date):
        logger_index = -1
        with open(self.path, 'r') as file:
            file_data = json.load(file)
            for day in file_data:
                if day["Date"] == date:
                    logger_index = file_data.index(day)
        return logger_index