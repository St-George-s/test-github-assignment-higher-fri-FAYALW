#Imports
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


#Showing the menu
def showMenu():
    print("1 - Add task")
    print("2 - Delete task")      
    print("3 - Mark task")      
    print("4 - View by category")      
    print("5 - Quit program")


#FR1 - ADDING A TASK
def insertTask(cur, taskName, category, dueDate, completionStatus):
    sql = """
    INSERT INTO Tasks( 
    taskName,  
    category, 
    dueDate, 
    completionStatus
    ) 
    VALUES(
        %s, 
        %s, 
        %s, 
        %s
    )
    """
    cur.execute(sql, (taskName, category, dueDate, completionStatus, ))
    conn.commit()


#FR2 - USING AN ARRAY OF RECORDS TO STORE AND DISPLAY TASK DATA
class Task:
    def __init__(self, taskID, taskName, category, dueDate, completionStatus):
        self.taskID = taskID
        self.taskName = taskName
        self.category = category
        self.dueDate = dueDate
        self.completionStatus = completionStatus

def buildArray():
    cur.execute("SELECT * FROM Tasks")
    rows = cur.fetchall()
    tasks_array = rows

tasksArray = buildArray()


#FR3&4 - USING & APPLYING A BUBBLE SORT
def sortTasksByStatus(tasksArray):
    n = len(tasksArray)
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(0, n-1):
            if tasksArray[i].completionStatus == True:
                tasksArray[i], tasksArray[i+1] = tasksArray[i+1], tasksArray[i]
                swapped = True
        n-=1


#FR5 - DATABASE


#FR6 - DELETING A TASK
def deleteTask(taskToDelete):
    sql = """
    DELETE FROM Tasks
    WHERE taskID = taskToDelete
    """
    cur.execute(sql, )
    conn.commit()

#FR7 - UID
conn, cur = open_db()
showTasks(cur)
showMenu()
option = int(input("Enter option: "))
if option == 1:
    taskName = input("Enter task name: ")
    insertTask(cur, taskName)
    category = input("Enter category name: ")
    insertTask(cur, category)
    dueDate = input("Enter due date: ")
    insertTask(cur, dueDate)
    completionStatus = input("Is the task complete? True or False: ")
    insertTask(cur, completionStatus)

if option == 2:
    taskToDelete = input("Enter the task ID of the task you wish to delete: ")
    deleteTask(cur, taskToDelete)


if option == 3:
    taskToMark = input("Enter the task ID of the task you wish to mark: ")
    markTask(cur, taskToMark)


if option == 4:
    categoryToDisplay = input("Enter the category of the tasks you wish to be displayed: ")
    viewByCategory(cur, categoryToDisplay)

if option == 5:
    quit()


#FR8 - MARKING A TASK
def markTask(taskToMark):
    sql = """
    SELECT task
    FROM Tasks
    WHERE taskID = taskToMark
    """
    cur.execute(sql, )
    conn.commit()

#FR9 - VIEWING BY CATEGORY
def viewByCategory(categoryToDisplay):
    sql = """
    SELECT task
    FROM Tasks
    WHERE category = categoryToDisplay
    """
    cur.execute(sql, )
    conn.commit()


#FR10 - BLANK VALIDATION
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
