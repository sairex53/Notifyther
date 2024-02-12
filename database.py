import sqlite3
import os

def add_reminder_to_database(reminder: str, hour: int, minute: int, day: int, month: int, year: int):
    db = sqlite3.connect("reminder-database.db")
    c = db.cursor()

    c.execute(f"INSERT INTO articles VALUES ('{reminder}', {hour}, {minute}, {day}, {month}, {year})")
    
    db.commit()
    db.close()

def create_database_and_table():
    db = sqlite3.connect("reminder-database.db")
    c = db.cursor()

    c.execute("""CREATE TABLE articles (reminder text, hour integer, minute integer, day integer, month integer, year integer)""")
    db.commit()
    db.close()
    print("Database successfully created")

def check_exists_database() -> bool:
    if os.path.isfile("reminder-database.db"):
        print("File is exists")
        return True
    else:
        print("File doesn't exists")
        return False

def load_info_from_database(position: int):
    db = sqlite3.connect("reminder-database.db")
    c = db.cursor()
    c.execute("SELECT * FROM articles")
    
    data = c.fetchall()[position]
    output = (str(data[0]) + " | " + str(data[1]) + ":" + str(data[2]) + " | " + str(data[3]) + "." + str(data[4]) + "." + str(data[5]))
    #print(all_data)
    #       OR
    #data = c.fetchone()[1]
    db.commit()
    db.close()
    return output

def get_quanity():
    db = sqlite3.connect("reminder-database.db")
    c = db.cursor()
    info = c.execute('SELECT reminder FROM articles').fetchall()
    print('Items - ' + str(len(info)))
    return len(info)

def delete_item(text: str):
    db = sqlite3.connect("reminder-database.db")
    c = db.cursor()

    c.execute(f"DELETE FROM articles WHERE reminder='{text}'")
    db.commit()
    db.close()