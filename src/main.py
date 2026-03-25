import argparse
from rich import print
from pathlib import Path
import keyboard
import sys
from src.report import Report
from src.display import Display
from src.logger import Logger
import os

def terminate(display, logger):
    logger.empty_file()
    display.live.stop()
    display.console.print("exit program and flush the log :)")
    sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--interval', type=int, help="Enter an interval", default=2)
    parser.add_argument("--log", type=str, help="Enter an path for the folder of the logger file")
    parser.add_argument("--cpu_warn", type=int, help="Enter a percentage number for cpu warn", default=80)
    parser.add_argument("--mem_warn", type=int, help="Enter a percentage number for mem warn", default=80)
    parser.add_argument("--date", type=str, help="Enter a date for daily report for exa : 18/03/2026", default="")
    args = parser.parse_args()

    interval = args.interval
    path = args.log
    cpu_warn = args.cpu_warn
    mem_warn = args.mem_warn
    report_date = args.date

    if (os.path.exists(path)):
        logger_file = Path(path).joinpath("logger.json")
        logger = Logger(logger_file)
        logger.init_file()
    else:
        print("Invaild path for logger")

    if (report_date != ""):
        report = Report(logger_file, report_date, logger)
        print(report.report if not report.report == None else "Cannot found daily report in this date")
        sys.exit(0)

    try:
        display = Display(interval, cpu_warn, mem_warn, logger_file)
        keyboard.add_hotkey('ctrl+c', terminate, args=(display, logger))
    except KeyboardInterrupt:
        terminate(display, logger)
