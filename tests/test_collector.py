class Memory:
    def __init__(self):
        self.total = "31.9G"
        self.available = "18.7G"
        self.used = "13.3G"
        self.percent = 41.5
        self.free = "18.7G"

class Part:
    def __init__(self, num):
        if num == 1:
            self.device = "C:\\"
            self.fstype = "NTFS"
            self.mountpoint = "C:\\"
        if num == 2:
            self.device = "F:\\"
            self.fstype = "NTFS"
            self.mountpoint = "F:\\"

class Usage:
    def __init__(self, num):
        if num == 1:
            self.total = "476.4G"
            self.used = "438.3G"
            self.free = "38.1G"
            self.percent = "92%"
        if num == 2:
            self.total = "931.5G"
            self.used = "737.1G"
            self.free = "194.4G"
            self.percent = "79%"

def getCPUData():
    # return dictionary with cpu data
    data = {}
    data['cores'] = cpu_count(logical=False)
    data['threads'] = cpu_count(logical=True)
    data['cpu_per'] = cpu_percent(percpu=False)
    data['cpu_per_per'] = cpu_percent(percpu=True)
    data['freq'] = cpu_freq(percpu=True)
    return data

def cpu_count(logical):
    return 8 if logical else 4

def cpu_percent(percpu):
    l = [12.4, 15.4, 10.2, 28.2, 7.4, 8.3, 4.5]
    return l if percpu else round(sum(l) / len(l), 1)

def cpu_freq(percpu):
    return [4024.0]

def getMemory():
    # return dictionary with memory data
    virt_mem = virtual_memory()
    data = [
        virt_mem.total,
        virt_mem.available,
        virt_mem.used,
        virt_mem.percent,
        virt_mem.free
    ]
    return data

def virtual_memory():
    mem = Memory()
    return mem

def getDiskUsage():
    # return list with disk usage
    data = []
    disks = [[Part(1), Usage(1)], [Part(2), Usage(2)]]
    for disk in disks:
        data.append([
            disk[0].device,
            disk[1].total,
            disk[1].used,
            disk[1].free,
            disk[1].percent,
            disk[0].fstype,
            disk[0].mountpoint
        ])
    return data

def test_collect():
    assert getCPUData() == {
        'cores' : 4,
        'threads' : 8,
        'cpu_per' : 12.3,
        'cpu_per_per' : [12.4, 15.4, 10.2, 28.2, 7.4, 8.3, 4.5],
        'freq' : [4024.0]
    }
    assert getMemory() == [
        "31.9G",
        "18.7G",
        "13.3G",
        41.5,
        "18.7G"
    ]
    assert getDiskUsage() == [
        [
            "C:\\",
            "476.4G",
            "438.3G",
            "38.1G",
            "92%",
            "NTFS",
            "C:\\"
        ],
        [
            "F:\\",
            "931.5G",
            "737.1G",
            "194.4G",
            "79%",
            "NTFS",
            "F:\\"
        ]
    ]