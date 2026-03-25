from src.report import *
from src.logger import *

threshold_expected_data = {
    'CPU': 
        {'CPU Percentage': {'Minimum': 4.8, 'Avg': 25.825, 'Maximum': 75.0}, 
        'Thread 1': {'Minimum': 10.3, 'Avg': 32.2, 'Maximum': 66.7}, 
        'Thread 2': {'Minimum': 0.0, 'Avg': 28.125, 'Maximum': 100.0}, 
        'Thread 3': {'Minimum': 4.6, 'Avg': 31.625, 'Maximum': 100.0}, 
        'Thread 4': {'Minimum': 4.6, 'Avg': 21.3, 'Maximum': 66.7}, 
        'Thread 5': {'Minimum': 6.2, 'Avg': 26.05, 'Maximum': 66.7}, 
        'Thread 6': {'Minimum': 1.5, 'Avg': 20.175, 'Maximum': 66.7}, 
        'Thread 7': {'Minimum': 3.1, 'Avg': 21.35, 'Maximum': 66.7}, 
        'Thread 8': {'Minimum': 7.7, 'Avg': 25.225, 'Maximum': 66.7}, 
        'Frequency Thread 1': {'Minimum': 4201.0, 'Avg': 4201.0, 'Maximum': 4201.0}
    }, 
    'Memory': 
        {'Available': {'Minimum': 18.7, 'Avg': 18.7, 'Maximum': 18.7}, 
        'Used': {'Minimum': 13.3, 'Avg': 13.3, 'Maximum': 13.3}, 
        'Percent': {'Minimum': 41.5, 'Avg': 41.574999999999996, 'Maximum': 41.6}, 
        'Free': {'Minimum': 18.7, 'Avg': 18.7, 'Maximum': 18.7}
    }, 
    'Disk Usage': 
        {'C:\\': 
            {'Used': {'Minimum': 438.3, 'Avg': 438.3, 'Maximum': 438.3}, 
            'Free': {'Minimum': 38.1, 'Avg': 38.1, 'Maximum': 38.1}, 
            'Use': {'Minimum': 92.0, 'Avg': 92.0, 'Maximum': 92.0}}, 
        'F:\\': {'Used': {'Minimum': 737.1, 'Avg': 737.1, 'Maximum': 737.1}, 
                'Free': {'Minimum': 194.4, 'Avg': 194.4, 'Maximum': 194.4}, 
                'Use': {'Minimum': 79.0, 'Avg': 79.0, 'Maximum': 79.0}}
        }
    }

def test_logger():
    rep = Report(r"C:/Users/raz/Desktop/project/SysMon/src/logger.json", "19/03/2026", Logger(r"C:/Users/raz/Desktop/project/SysMon/src/logger.json"))
    data = {
        "Date": "19/03/2026",
        "CPU": [
            {
                "Num Cores": 4,
                "Num Threads": 8,
                "CPU Percentage": "75.0%",
                "Thread 1": "66.7%",
                "Thread 2": "100.0%",
                "Thread 3": "100.0%",
                "Thread 4": "66.7%",
                "Thread 5": "66.7%",
                "Thread 6": "66.7%",
                "Thread 7": "66.7%",
                "Thread 8": "66.7%",
                "Frequency Thread 1": 4201.0
            },
            {
                "Num Cores": 4,
                "Num Threads": 8,
                "CPU Percentage": "13.1%",
                "Thread 1": "26.1%",
                "Thread 2": "7.8%",
                "Thread 3": "9.4%",
                "Thread 4": "9.2%",
                "Thread 5": "18.8%",
                "Thread 6": "7.8%",
                "Thread 7": "9.4%",
                "Thread 8": "15.6%",
                "Frequency Thread 1": 4201.0
            },
            {
                "Num Cores": 4,
                "Num Threads": 8,
                "CPU Percentage": "4.8%",
                "Thread 1": "10.3%",
                "Thread 2": "0.0%",
                "Thread 3": "4.6%",
                "Thread 4": "4.6%",
                "Thread 5": "6.2%",
                "Thread 6": "1.5%",
                "Thread 7": "3.1%",
                "Thread 8": "7.7%",
                "Frequency Thread 1": 4201.0
            },
            {
                "Num Cores": 4,
                "Num Threads": 8,
                "CPU Percentage": "10.4%",
                "Thread 1": "25.7%",
                "Thread 2": "4.7%",
                "Thread 3": "12.5%",
                "Thread 4": "4.7%",
                "Thread 5": "12.5%",
                "Thread 6": "4.7%",
                "Thread 7": "6.2%",
                "Thread 8": "10.9%",
                "Frequency Thread 1": 4201.0
            }
        ],
        "Memory": [
            {
                "Total": "31.9G",
                "Available": "18.7G",
                "Used": "13.3G",
                "Percent": "41.6%",
                "Free": "18.7G"
            },
            {
                "Total": "31.9G",
                "Available": "18.7G",
                "Used": "13.3G",
                "Percent": "41.5%",
                "Free": "18.7G"
            },
            {
                "Total": "31.9G",
                "Available": "18.7G",
                "Used": "13.3G",
                "Percent": "41.6%",
                "Free": "18.7G"
            },
            {
                "Total": "31.9G",
                "Available": "18.7G",
                "Used": "13.3G",
                "Percent": "41.6%",
                "Free": "18.7G"
            }
        ],
        "Disk Usage": [
            [
                {
                    "Device": "C:\\",
                    "Total": "476.4G",
                    "Used": "438.3G",
                    "Free": "38.1G",
                    "Use": "92%",
                    "Type": "NTFS",
                    "Mount": "C:\\"
                },
                {
                    "Device": "F:\\",
                    "Total": "931.5G",
                    "Used": "737.1G",
                    "Free": "194.4G",
                    "Use": "79%",
                    "Type": "NTFS",
                    "Mount": "F:\\"
                }
            ],
            [
                {
                    "Device": "C:\\",
                    "Total": "476.4G",
                    "Used": "438.3G",
                    "Free": "38.1G",
                    "Use": "92%",
                    "Type": "NTFS",
                    "Mount": "C:\\"
                },
                {
                    "Device": "F:\\",
                    "Total": "931.5G",
                    "Used": "737.1G",
                    "Free": "194.4G",
                    "Use": "79%",
                    "Type": "NTFS",
                    "Mount": "F:\\"
                }
            ],
            [
                {
                    "Device": "C:\\",
                    "Total": "476.4G",
                    "Used": "438.3G",
                    "Free": "38.1G",
                    "Use": "92%",
                    "Type": "NTFS",
                    "Mount": "C:\\"
                },
                {
                    "Device": "F:\\",
                    "Total": "931.5G",
                    "Used": "737.1G",
                    "Free": "194.4G",
                    "Use": "79%",
                    "Type": "NTFS",
                    "Mount": "F:\\"
                }
            ],
            [
                {
                    "Device": "C:\\",
                    "Total": "476.4G",
                    "Used": "438.3G",
                    "Free": "38.1G",
                    "Use": "92%",
                    "Type": "NTFS",
                    "Mount": "C:\\"
                },
                {
                    "Device": "F:\\",
                    "Total": "931.5G",
                    "Used": "737.1G",
                    "Free": "194.4G",
                    "Use": "79%",
                    "Type": "NTFS",
                    "Mount": "F:\\"
                }
            ]
        ]
    }
    threshold_data = {

    }
    threshold_data['CPU'] = rep.get_cpu_report(data['CPU'])
    threshold_data['Memory'] = rep.get_memory_report(data['Memory'])
    threshold_data['Disk Usage'] = rep.get_disk_usage_report(data['Disk Usage'])
    assert threshold_expected_data == threshold_data
    

