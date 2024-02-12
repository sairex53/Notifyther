import subprocess
import os
import time
import sys
from datetime import datetime
from PyQt5.QtWidgets import QInputDialog

def send_notification(reminder: str):
    script_runner = "osascript -e '"
    script_body = f'display notification "{reminder}" with title "Reminder" sound name "Submarine"' + "'"
    cmd = script_runner + script_body
    os.system(cmd)

def validate_time(alarm_time):
    if len(alarm_time) != 8:
        print("Error")
    else:
        if int(alarm_time[0:2]) > 23:
            print("Error")
        elif int(alarm_time[3:5]) > 59:
            print("Error")
        elif int(alarm_time[6:8]) > 59:
            print("Error")
        else:
            return "Okey"

