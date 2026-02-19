#MENU
import mysql.connector
from dataclasses import dataclass
from typing import List, Optional
from datetime import date
from datetime import datetime

#Database configuration
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "student",
    "password": "studentpw",
    "database": "project1",
    "port": 3306
}


#FR2 - Record structure/array of records
class Task:
    taskID: int
    taskName: str
    category: str
    dueDate: int
    completionStatus: str


#Database helpers
def open_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    return conn, cur

def close_db(conn, cur):
    cur.close()
    conn.close()

#Showing all tasks
def showTasks(cur):
    sql = """
    SELECT taskID,
           taskName,
           category,
           dueDate,
           completionStatus
    FROM Tasks;
    """
    cur.execute(sql, )
    rows = cur.fetchall()
    print(rows)

#Showing all tasks
def showSpecificTask(cur):
    sql = """
    SELECT taskID,
           taskName,
           category,
           dueDate,
           completionStatus
    FROM Tasks
    WHERE taskID = %s AND category = %s;
    """
    cur.execute(sql, (3,"Household"))
    rows = cur.fetchall()
    print(rows)

#Showing all tasks
def insertTask(cur, taskName):
    sql = """
    INSERT INTO Tasks
    ( 
    taskName,  
    category, 
    dueDate, 
    completionStatus
    ) VALUES(
        %s, 
        3, 
        "Household", 
        "2026-12-12", 
        TRUE
    )
    """
    cur.execute(sql, (taskName, ))
    conn.commit()

#Menu and input validation
def showMenu():
    print("1 - Add task")
    print("2 - Delete task")      
    print("3 - Mark task")      
    print("4 - View by category")      
    print("5 - Quit program")


conn, cur = open_db()
showTasks(cur)
showMenu()
option = int(input("Enter option: "))
if option == 1:
    taskName = input("Enter task name: ")
    insertTask(cur, taskName)


#FR1 - ADDING TASK


#FR2 - DISPLAYING TASK DATA


#FR3&4 - USING A BUBBLE SORT


#FR5 - DATABASE


#FR6 - DELETING TASK


#FR7 - UID
# showMenu
# number = input("Please enter a number 1-5: ")
# if number == 1:
#     taskName = input("Please enter the name of your task: ")
#     category = input("Please enter the category of your task: ")
#     dueDate = input("Please enter the due date of your task: ")

# if number == 2:
#     taskToDelete = input("Please enter the task ID of the task that you wish to delete: ")

# if number == 3:
#     chosenTaskID = input("Please enter the task ID of the task that you wish to mark: ")

# if number == 4:
#     chosenCategory = input("Please enter the category of task that you would like to view: ")

# if number == 5:
#     quit()


# #FR8 - MARKING TASK


# #FR9 - VIEWING BY CATEGORY


# #FR10 - BLANK VALIDATION
def isFieldBlank(input):
    if not input:
        print("Please enter something: ")


#FR11 - DATE VALIDATION
def isDateValid(date_string: str, fmt: str = "%Y-%m-%d") -> bool:
    try:
        datetime.strptime(date_string, fmt)
        return True
    except ValueError:
        return False


#MAIN - CALLING ALL FUNCTIONS