import sys
import time
import subprocess
import os
from datetime import datetime
import threading 
from PyQt5 import QtCore, QtGui, QtWidgets
from app import Ui_MainWindow
from database import get_quanity, load_info_from_database, add_reminder_to_database, check_exists_database, create_database_and_table, delete_item
from notification import validate_time, send_notification
from editReminder import Ui_edit_reminder
from warning import Ui_Dialog

def load_items():
    #Get quanity lines from database
    quanity_items = get_quanity()

    #Load database to list items
    b = 0
    while b < quanity_items:
        data = str(load_info_from_database(b))
        data = data.replace('(', '')
        data = data.replace(')', '')
        data = data.replace("'", '')
        #print(data[2])
        print(data)
        ui.listWidget.addItem(str(data))
        b = b + 1

def plan_alarm(reminder_time: str, reminder: str) -> bool:
    while True:
        alarm_time = reminder_time #Example - '02:45:00'
        validate = validate_time(alarm_time)
        if validate != "Okey":
            print(validate)
        else:
            print("Alarm accepted")
            break

    alarm_hour = int(alarm_time[0:2])
    alarm_minutes = int(alarm_time[3:5])

    while True:
        now = datetime.now()
        current_hour = now.hour
        current_minuetes = now.minute
        
        if alarm_hour == current_hour:
            if alarm_minutes == current_minuetes:
                send_dialog()
                #send_notification() 
                #break
    #return True

def send_dialog(reminder: str) -> bool:
    while True:
        send_notification(reminder)

        cmd  = subprocess.run(['/usr/bin/osascript', 'dialog.scpt'], capture_output = True, text=True) 
        #/Users/elliot/code/Python/Notifyther/R5/ 100% working path
        output = str(cmd.stdout)
        if output == "«class bhit»:Complete\n":
            print("log: Complete")    
            break

        elif output == "«class bhit»:Through 15m\n": 
            print("log: Remind me in 15 minutes")
            time.sleep(900)

        elif output == "«class bhit»:Through 1h\n":
            print("log: Remind me in 1 hour")
            time.sleep(3600)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def change_dateTime():
    #Change time to real time
    now = datetime.now()
    hour = int(now.strftime("%H"))
    minutes = int(now.strftime("%M"))
    print("Time - ", hour, minutes)
    ui.timeEdit.setTime(QtCore.QTime(hour, minutes, 0))
    #Change date to real date
    year = int(datetime.today().strftime('%Y'))
    month = int(datetime.today().strftime('%m'))
    day = int(datetime.today().strftime('%d'))
    print("Date - ", year, month, day)
    #Set date
    ui.dateEdit.setDate(QtCore.QDate(year, month, day))

def check_database():
    if check_exists_database() == True:
        pass
    elif check_exists_database() == False:
        create_database_and_table()

def show_through(hour: int, minutes: int, day: int, month: int, year: int):
    reminder = ui.EditText.text()

    now = datetime.now()
    hour_now = now.hour
    minutes_now = now.minute
    day_now = now.day
    month_now = now.month
    year_now = now.year

    print(str(hour_now) + ":" + str(minutes_now) + " | " + str(day_now) + "." + str(month_now) + "." + str(year_now))

    print("Remind accepted - ", str(hour) + ":" + str(minutes) + " | " + str(day) + "." + str(month) + "." + str(year))
    
    while True:
        now = datetime.now()
        hour_now = now.hour
        minutes_now = now.minute
        day_now = now.day
        month_now = now.month
        year_now = now.year

        file_path = os.path.realpath(__file__)
        #Programm dir 
        work_dir = os.path.dirname(file_path)

        if os.path.isfile(work_dir + "/close.w2p"):
            print("Remind closed")
            break

        if year_now == year_now:
            if month_now == month:
                if day_now == day:
                    if hour_now == hour:
                        if minutes_now == minutes:
                            send_dialog(reminder)
                            print("Remind notifyed")
                            break

def add_reminder():
    current_day = ui.dateEdit.date().day()
    current_month = ui.dateEdit.date().month()
    current_year = ui.dateEdit.date().year()

    current_hour = ui.timeEdit.time().hour()
    current_minute = ui.timeEdit.time().minute()
    print(current_hour, '\n', current_minute)

    # index = ui.listWidget.currentRow()
    # ui.listWidget.item(index).setText(data)

    reminder = ui.EditText.text()
    ui.EditText.setText("")
    data = str(reminder) + " | " + str(current_hour) + ":" + str(current_minute) + " | " + str(current_day) + "." + str(current_month) + "." + str(current_year) 
    ui.listWidget.addItem(data)

    add_reminder_to_database(reminder, current_hour, current_minute, current_day, current_month, current_year)
    print(f"Saved - {reminder, current_hour, current_minute, current_day, current_month, current_year}")
    
    show_through(current_hour, current_minute, current_day, current_month, current_year)

def clear_edittext():
    ui.EditText.setText(" ")

def remove_reminder():
    # ADD DISABLE REMINDER THREAD
    currentIndex = ui.listWidget.currentRow()
    
    #Delete item from database
    item_choice = ui.listWidget.item(currentIndex).text()
    print("Deleted - ", item_choice)
    get_text_remind = item_choice.split(' | ')
    remind_text = get_text_remind[0]
    if remind_text == " ":
        print("None")
        delete_item(0)
    else:
        delete_item(remind_text)

    item = ui.listWidget.takeItem(currentIndex)
    del item

def thread_add_reminder():
    t1=threading.Thread(target=add_reminder)
    t1.start()

def edit_item():    
    global OtherWindow 
    OtherWindow = QtWidgets.QDialog()
    ui2 = Ui_edit_reminder()
    ui2.setupUi(OtherWindow)
    
    def load_componentsEdit():
        #Change time to real time
        now = datetime.now()
        hour = int(now.strftime("%H"))
        minutes = int(now.strftime("%M"))
        print("Time - ", hour, minutes)
        ui2.timeEdit.setTime(QtCore.QTime(hour, minutes, 0))
        #Change date to real date
        year = int(datetime.today().strftime('%Y'))
        month = int(datetime.today().strftime('%m'))
        day = int(datetime.today().strftime('%d'))
        print("Date - ", year, month, day)
        #Set date
        ui2.dateEdit.setDate(QtCore.QDate(year, month, day))

    def stop_remind():
        file_path = os.path.realpath(__file__)
        work_dir = os.path.dirname(file_path)
        f = open(work_dir + "/close.w2p", mode="w")
        f.write(" ")
        f.close()
        os.system("/bin/rm -rf " + work_dir + "/close.w2p")

    def add_reminder_fromEditWindow():
        current_day = ui2.dateEdit.date().day()
        current_month = ui2.dateEdit.date().month()
        current_year = ui2.dateEdit.date().year()

        current_hour = ui2.timeEdit.time().hour()
        current_minute = ui2.timeEdit.time().minute()
        print(current_hour, '\n', current_minute)

        # index = ui.listWidget.currentRow()
        # ui.listWidget.item(index).setText(data)

        reminder = ui2.editText.text()
        data = str(reminder) + " | " + str(current_hour) + ":" + str(current_minute) + " | " + str(current_day) + "." + str(current_month) + "." + str(current_year) 
        ui.listWidget.addItem(data)

        add_reminder_to_database(reminder, current_hour, current_minute, current_day, current_month, current_year)
        print(f"Saved - {reminder, current_hour, current_minute, current_day, current_month, current_year}")
        
        show_through(current_hour, current_minute, current_day, current_month, current_year)
        ui2.editText.setText("")
    
    def edit_reminder():
        stop_remind()
        remove_reminder()
        t2 = threading.Thread(target=add_reminder_fromEditWindow)
        t2.start()
        OtherWindow.close()

    def close_editWindow():
        OtherWindow.close()

    load_componentsEdit()

    ui2.btn_accept.clicked.connect(edit_reminder)
    ui2.btn_close.clicked.connect(close_editWindow)
    OtherWindow.show()

    #ui.listWidget.item(index).setText() 

def check_FileClearRemindList():
    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)
    if os.path.isfile(work_dir + "/clearList.iso"):
        ui.checkBox.setChecked(True)
        print("CheckBox is True")
    else:
        load_items()

def checkbox_accept():
    global WarningWindow
    WarningWindow = QtWidgets.QDialog()
    ui3 = Ui_Dialog()
    ui3.setupUi(WarningWindow)
    WarningWindow.show()

    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)

    if ui.checkBox.isChecked() == True:
        f = open(work_dir + "/clearList.iso", mode="w")
        f.write(" ")
        f.close()
    elif ui.checkBox.isChecked() == False:
        os.system("/bin/rm -rf " + work_dir + "/clearList.iso")
    
#Connect buttons
ui.btn_add.clicked.connect(thread_add_reminder)
ui.btn_remove.clicked.connect(remove_reminder)
ui.btn_clear.clicked.connect(clear_edittext)
ui.btn_edit.clicked.connect(edit_item)
ui.checkBox.clicked.connect(checkbox_accept)

check_database()
change_dateTime()
check_FileClearRemindList()

sys.exit(app.exec_())
