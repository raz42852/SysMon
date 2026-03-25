import os
import json

def test_logger():
    filepath = os.path.join(os.getcwd(), 'test.json')
    if not os.path.exists(filepath):
        f = open(filepath, "a")
    data = [
        {
            "Date": "17/03/2026",
            "CPU": [],
            "Memory": [],
            "Disk Usage": []
        },
        {
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
        },
        {
            "Date": "20/03/2026",
            "CPU": [],
            "Memory": [],
            "Disk Usage": []
        }
    ]
    with open(filepath, 'w') as file:
        json.dump(data, file)
    with open(filepath, 'r') as file:
        assert data == json.load(file)
