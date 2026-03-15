import psutil
from psutil._common import bytes2human

def getCPUData():
    # return dictionary with cpu data
    data = {}
    data['cores'] = psutil.cpu_count(logical=False)
    data['threads'] = psutil.cpu_count(logical=True)
    data['cpu_per'] = psutil.cpu_percent(interval=1, percpu=True)
    data['freq'] = psutil.cpu_freq(percpu=True)
    return data

def getMemory():
    # return dictionary with memory data
    virt_mem = psutil.virtual_memory()
    data = {
        "total" : bytes2human(virt_mem.total),
        "available" : bytes2human(virt_mem.available),
        "used" : bytes2human(virt_mem.used),
        "percent" : bytes2human(virt_mem.percent),
        "free" : bytes2human(virt_mem.free)
    }
    return data
    
def getDiskUsage():
    # return dictionary with disk usage
    data = {
        "device" : [],
        "total" : [],
        "used" : [],
        "free" : [],
        "use" : [],
        "type" : [],
        "mount" : [],
    }
    for part in psutil.disk_partitions(all=False):
        if 'cdrom' in part.opts or not part.fstype:
            # skip cd-rom drives with no disk in it; they may raise
            # ENOENT, pop-up a Windows GUI error for a non-ready
            # partition or just hang.
            continue
        usage = psutil.disk_usage(part.mountpoint)
        data["device"].append(part.device)
        data["total"].append(bytes2human(usage.total))
        data["used"].append(bytes2human(usage.used))
        data["free"].append(bytes2human(usage.free))
        data["use"].append(int(usage.percent))
        data["type"].append(part.fstype)
        data["mount"].append(part.mountpoint)
    return data