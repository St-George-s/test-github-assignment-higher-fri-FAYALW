import mysql.connector
from dataclasses import dataclass
from typing import List, Optional


#Database configuration
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "student",
    "password": "studentpw",
    "database": "project1",
    "port": 3306
}


#Record structure/array of records
class Task:
    taskID: int
    taskName: str
    categoryID: int
    category: str
    dueDate: int
    completionSatus: str


#Database helpers
def open_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    return conn, cur

def close_db(conn, cur):
    cur.close()
    conn.close()


#Showing all tasks
def showTasks():
    sql = """
    SELECT taskID,
           taskName,
           categoryID,
           category,
           dueDate,
           completionSatus
    FROM Tasks
    """


#Menu and input validation
def showMenu():
    print("1 - Add task")
    print("2 - Delete task")      
    print("3 - Mark task")      
    print("4 - View by category")      
    print("5 - Quit program")