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
def insertTask(cur, taskName, category, dueDate, ):
    sql = """
    INSERT INTO Tasks( 
    taskName,  
    category, 
    dueDate
    ) 
    VALUES(
        %s, 
        %s, 
        %s, 
    )
    """
    cur.execute(sql, (taskName, category, dueDate, ))
    conn.commit()


#FR2 - USING AN ARRAY OF RECORDS TO STORE AND DISPLAY TASK DATA
class Task:
    def __init__(self, taskID, taskName, category, dueDate, completionStatus):
        self.taskID = taskID
        self.taskName = taskName
        self.category = category
        self.dueDate = dueDate
        self.completionStatus = completionStatus

def buildArray(cur):
    cur.execute("SELECT * FROM Tasks")
    rows = cur.fetchall()

    tasks_array = []

    for row in rows:
        task = Task(
            taskID=row[0],
            taskName=row[1],
            category=row[2],
            dueDate=row[3],
            completionStatus=bool(row[4])
        )
        tasks_array.append(task)

    return tasks_array

conn, cur = open_db()
tasksArray = buildArray(cur)


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
def deleteTask(cur, taskToDelete):
    sql = """
    DELETE FROM Tasks
    WHERE taskID = %s
    """
    cur.execute(sql, (taskToDelete, ))
    conn.commit()


#FR8 - MARKING A TASK
def markTask(cur, taskToMark):
    sql = """
    UPDATE Tasks
    SET completionStatus = NOT completionStatus
    WHERE taskID = %s
    """
    
    cur.execute(sql, (taskToMark,))
    conn.commit()


#FR9 - VIEWING BY CATEGORY    
def viewByCategory(cur, categoryToDisplay):
    sql = """
    SELECT *
    FROM Tasks
    WHERE category = %s
    """
    cur.execute(sql, (categoryToDisplay, ))


#FR10 - BLANK VALIDATION
def isFieldBlank(input):
    if not input:
        return True
    return False


#FR11 - DATE VALIDATION
def isDateValid(date_string: str, fmt: str = "%Y-%m-%d") -> bool:
    try:
        datetime.strptime(date_string, fmt)
        return True
    except ValueError:
        return False
    

#FR7 - UID
conn, cur = open_db()
showTasks(cur)
showMenu()
option = int(input("Enter option: "))
if option == 1:
    taskName = input("Enter task name: ")
    while isFieldBlank(taskName) == True:
        print("Please enter something")
        
    category = input("Enter category name: ")
    while isFieldBlank(category) == True:
        print("Please enter something")
    dueDate = input("Enter due date: ")
    while isFieldBlank(dueDate) == True and isDateValid(dueDate) == True:
        print("Please enter something")
    completionStatus = False
    insertTask(cur, taskName, category, dueDate, )


if option == 2:
    taskToDelete = input("Enter the task ID of the task you wish to delete: ")
    deleteTask(cur, taskToDelete)


if option == 3:
    taskToMark = input("Enter the task ID of the task you wish to mark: ")
    if completionStatus.lower() == "true":
        completionStatus = True
    else:
        completionStatus = False
    markTask(cur, taskToMark)


if option == 4:
    categoryToDisplay = input("Enter the category of the tasks you wish to be displayed: ")
    viewByCategory(cur, categoryToDisplay)


if option == 5:
    quit()