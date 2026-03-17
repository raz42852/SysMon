import psutil
from psutil._common import bytes2human

def getCPUData():
    # return dictionary with cpu data
    data = {}
    data['cores'] = psutil.cpu_count(logical=False)
    data['threads'] = psutil.cpu_count(logical=True)
    data['cpu_per'] = psutil.cpu_percent(percpu=False)
    data['cpu_per_per'] = psutil.cpu_percent(percpu=True)
    data['freq'] = psutil.cpu_freq(percpu=True)
    return data

def getMemory():
    # return dictionary with memory data
    virt_mem = psutil.virtual_memory()
    data = [
        bytes2human(virt_mem.total),
        bytes2human(virt_mem.available),
        bytes2human(virt_mem.used),
        f"{virt_mem.percent}%",
        bytes2human(virt_mem.free)
    ]
    return data
    
def getDiskUsage():
    # return dictionary with disk usage
    data = []
    for part in psutil.disk_partitions(all=False):
        if 'cdrom' in part.opts or not part.fstype:
            # skip cd-rom drives with no disk in it; they may raise
            # ENOENT, pop-up a Windows GUI error for a non-ready
            # partition or just hang.
            continue
        usage = psutil.disk_usage(part.mountpoint)
        data.append([
            part.device,
            f"{bytes2human(usage.total)}",
            f"{bytes2human(usage.used)}",
            f"{bytes2human(usage.free)}",
            f"{int(usage.percent)}%",
            part.fstype,
            part.mountpoint
        ])
    return data