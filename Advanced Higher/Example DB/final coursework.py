#Imports
#Allows the program to connect to and interact with a MySQL database
import mysql.connector

#Allows the program to validate date inputs
from datetime import datetime


#Database configuration
#Dictionary storing database connection details
#Allows the program to connect to the MySQL database
DB_CONFIG = {
    "host": "127.0.0.1", #My computer
    "user": "student", #MySQL username
    "password": "studentpw", #MySQL password
    "database": "project1", #Database name
    "port": 3306 #Default MySQL port
}


#Database helpers
#Opens the database
def open_db():
    #Returns the connection and cursor objects
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    return conn, cur

#Closes the database
def close_db(conn, cur):
    cur.close()
    conn.close()


#Gets and displays all the records from the Tasks table
def showTasks(cur):
    sql = """
    SELECT taskID,
           taskName,
           category,
           dueDate,
           completionStatus
    FROM Tasks;
    """
    #Executes the SQL
    cur.execute(sql, )
    rows = cur.fetchall()
    print(rows)


#Shows the menu options
def showMenu():
    print("1 - Add task")
    print("2 - Delete task")      
    print("3 - Mark task")      
    print("4 - View by category")      
    print("5 - Quit program")


#FR1
#Inserts a new task into the database
def insertTask(conn, cur, taskName, category, dueDate, completionStatus, ):
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
    #Commits the changes
    conn.commit()


#FR2
#Creates a class to represent each task as an object, creating an array of Task objects
class Task:
    def __init__(self, taskID, taskName, category, dueDate, completionStatus):
        self.taskID = taskID
        self.taskName = taskName
        self.category = category
        self.dueDate = dueDate
        self.completionStatus = completionStatus


#Gets all the tasks from the database and stores them in an array of Task objects
def buildArray(cur):
    cur.execute("SELECT * FROM Tasks")
    rows = cur.fetchall()

    #Initialises the array
    tasks_array = []

    #Loops through the rows and converts to a Task object
    for row in rows:
        task = Task(
            taskID=row[0],
            taskName=row[1],
            category=row[2],
            dueDate=row[3],
            completionStatus=bool(row[4]) #Converts to a boolean
        )
        #Appends each object to the array
        tasks_array.append(task)

    return tasks_array


#Displays all tasks stored in the array of records
def displayTasksArray(tasksArray):
    for task in tasksArray:
        print(
            task.taskID,
            task.taskName,
            task.category,
            task.dueDate,
            task.completionStatus
        )


#Sorts the tasks so that completed tasks are sent to the end of the list and incomplete tasks appear first (FR3&FR4)
#Goes through the list, compares two elements at a time, swaps them if needed, continues until there are no more swaps to be had
def sortTasksByStatus(tasksArray):
    n = len(tasksArray)
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(0, n-1):
            #If the task is completed (True), swaps it with the next item so that the incomplete task appears first
            if tasksArray[i].completionStatus == True:
                tasksArray[i], tasksArray[i+1] = tasksArray[i+1], tasksArray[i]
                swapped = True
        #Reduced the range each pass
        n-=1


#Deletes a task from the database using the taskID as the primary key (FR6)
def deleteTask(conn, cur, taskToDelete):
    sql = """
    DELETE FROM Tasks
    WHERE taskID = %s
    """
    cur.execute(sql, (taskToDelete, ))
    conn.commit()


#Marks a task as complete or incomplete by toggling the completion status of the task (FR8)
#Uses SQL NOT operator to reverse the boolean value
def markTask(conn, cur, taskToMark):
    sql = """
    UPDATE Tasks
    SET completionStatus = NOT completionStatus
    WHERE taskID = %s
    """
    cur.execute(sql, (taskToMark, ))
    conn.commit()


#Displays only the tasks that match a specific category (FR9)    
def viewByCategory(cur, categoryToDisplay):
    sql = """
    SELECT *
    FROM Tasks
    WHERE category = %s
    """
    cur.execute(sql, (categoryToDisplay, ))
    rows = cur.fetchall()
    for row in rows:
        #Formats the output
        print(f"taskID: {row[0]} | taskName: {row[1]} | category: {row[2]} | dueDate: {row[3]} | completionStatus: {row[4]}")


#Checks if the input is blank, so prevents blank entries being added to the database (FR10)
def isFieldBlank(input):
    #Returns True if the field is empty
    if not input:
        return True
    return False


#Checks id the date entered matched the format YYYY-MM-DD (FR11)
def isDateValid(date_string: str, fmt: str = "%Y-%m-%d") -> bool:
    try:
        datetime.strptime(date_string, fmt)
        return True
    except ValueError:
        return False
    

#User interface (FR7)
#Opens the database
conn, cur = open_db()

#An infinite loop keeps the program running until the user chooses to quit it
while True:
    #Builds the array from the database
    tasksArray = buildArray(cur)

    #Sorts tasks using the bubble sort
    sortTasksByStatus(tasksArray)
    
    #Displays the sorted tasks
    displayTasksArray(tasksArray)

    #Shows the menu options
    showMenu()
    option = int(input("Enter an option number: "))
    while option not in [1,2,3,4,5]:
        print("Please enter something")

    #Option 1: Adding a task
    if option == 1:
        taskName = input("Enter a task name: ")
        while isFieldBlank(taskName):
            print("Please enter something")
            taskName = input("Enter a task name: ")
        category = input("Enter a category: ")
        while isFieldBlank(category):
            print("Please enter something")
            category = input("Enter a category: ")
        dueDate = input("Enter due date: ")
        while isFieldBlank(dueDate) or not isDateValid(dueDate):
            print("Enter a valid date (YYYY-MM-DD)")
            dueDate = input("Enter due date: ")
        completionStatus = False
        insertTask(conn, cur, taskName, category, dueDate, completionStatus, )

    
    #Option 2: Deleting a task
    if option == 2:
        taskToDelete = int(input("Enter the task ID of the task you wish to delete: "))
        deleteTask(conn, cur, taskToDelete)
        

    #Option 3: Marking a task
    if option == 3:
        taskToMark = input("Enter the task ID of the task you wish to mark: ")
        markTask(conn, cur, taskToMark)


    #Option 4: Displaying tasks within a specified category
    if option == 4:
        categoryToDisplay = input("Enter the category of the tasks you wish to be displayed: ")
        viewByCategory(cur, categoryToDisplay)


    #Option 5: Quit the program
    if option == 5:
        break


#Closes the database
close_db(conn, cur)
print("Database connection closed.")