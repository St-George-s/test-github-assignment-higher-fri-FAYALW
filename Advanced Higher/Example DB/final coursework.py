#Imports

#Allows the program to connect to and interact with a MySQL database
import mysql.connector

#Allows the program to display task data in a formatted table
from texttable import Texttable

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


#Opens a connection to the database
def open_db():
    #Connects to the database using the configuration dictionary
    conn = mysql.connector.connect(**DB_CONFIG)
    #Creates a cursor object to allow SQL commands to be executed
    cur = conn.cursor()
    #Returns the connection and cursor objects
    return conn, cur


#Closes the database connection
def close_db(conn, cur):
    #Closes the cursor and database connection
    cur.close()
    conn.close()


#Gets and displays all the records from the Tasks table
def showTasks(cur):
    #SQL query to select required columns from the Tasks table
    sql = """
    SELECT taskID,
           taskName,
           category,
           dueDate,
           completionStatus
    FROM Tasks;
    """
    #Executes the SQL query
    cur.execute(sql, )
    #Fetches all the rows returned from the query
    rows = cur.fetchall()
    print(rows)


#Displays the menu options
def showMenu():
    print("1 - Add task")
    print("2 - Delete task")      
    print("3 - Mark task")      
    print("4 - View by category")      
    print("5 - Quit program")


#FR1
#Inserts a new task into the database
def insertTask(conn, cur, taskName, category, dueDate, completionStatus, ):
    #SQL Query using placeholders (%s) so user input can be inserted
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
    #SQL query to get all the tasks from the Tasks table
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
    #Returns the completed list of Task objects
    return tasks_array


#Displays all tasks stored in the array of records in a table
def displayTasksArray(tasksArray):
    #Creates a table object
    table = Texttable()
    #Sets column alignment
    table.set_cols_align(["l", "l", "l", "l", "l"])
    #Adds the rows to the table
    table.add_rows(
        [["Task Number", "Task", "Category", "Due Date (YYYY-MM-DD)", "Completion Status"]] +
        [[task.taskID, task.taskName, task.category, task.dueDate,
        "Incomplete" if task.completionStatus == False else "Complete"]
        for task in tasksArray]
)
    print(table.draw())


#FR3&FR4
#Sorts the tasks so that completed tasks are sent to the end of the list and incomplete tasks appear first
def sortTasksByStatus(tasksArray):
    n = len(tasksArray)
    swapped = True
    #Goes through the list, compares two elements at a time, swaps them if needed, continues until there are no more swaps to be had
    while swapped:
        swapped = False
        for i in range(0, n-1):
            #If the task is completed (True), swaps it with the next item so that the incomplete task appears first
            if tasksArray[i].completionStatus == True:
                tasksArray[i], tasksArray[i+1] = tasksArray[i+1], tasksArray[i]
                swapped = True
        #Reduced the range each pass
        n-=1


#FR6
#Deletes a task from the database using the taskID as the primary key
def deleteTask(conn, cur, taskToDelete):
    sql = """
    DELETE FROM Tasks
    WHERE taskID = %s
    """
    cur.execute(sql, (taskToDelete, ))
    conn.commit()


#FR7
#User interface
#Opens the database
conn, cur = open_db()
def userInterface():
    #An infinite loop keeps the program running until the user chooses to quit it
    while True:
        #Calls function which builds the array from the database
        tasksArray = buildArray(cur)

        #Calls procedure which sorts tasks using the bubble sort
        sortTasksByStatus(tasksArray)
        
        #Calls procedure which displays the sorted tasks
        displayTasksArray(tasksArray)

        #Calls procedure which shows the menu options
        showMenu()

        #Gets the user option
        option = int(input("Enter an option number: "))
        #Ensures the option is valid
        while option not in [1,2,3,4,5]:
            print("Please enter a valid option")

        #Option 1: Adding a task
        if option == 1:
            taskName = input("Enter a task name: ")
            #Calls function to check that the user input is not blank
            while isFieldBlank(taskName):
                print("Please enter something")
                taskName = input("Enter a task name: ")

            category = input("Enter a category: ")
            while isFieldBlank(category):
                print("Please enter something")
                category = input("Enter a category: ")

            dueDate = input("Enter due date (YYYY-MM-DD): ")
            #Calls the function to check if the date is valid
            while isFieldBlank(dueDate) or not isDateValid(dueDate):
                print("Enter a valid date (YYYY-MM-DD)")
                dueDate = input("Enter due date: ")

            completionStatus = False
            #Calls the procedure to insert the task into the database and passes the required parameters
            insertTask(conn, cur, taskName, category, dueDate, completionStatus, )

        #Option 2: Deleting a task
        if option == 2:
            taskToDelete = int(input("Enter the task ID of the task you wish to delete: "))
            #Calls the procedure to delete a task from the database
            deleteTask(conn, cur, taskToDelete)
            
        #Option 3: Marking a task
        if option == 3:
            taskToMark = input("Enter the task ID of the task you wish to mark: ")
            #Calls the procedure to mark a task
            markTask(conn, cur, taskToMark)

        #Option 4: Displaying tasks within a specified category
        if option == 4:
            categoryToDisplay = input("Enter the category of the tasks you wish to be displayed: ")
            #Calls the procedure to view tasks by category
            viewByCategory(cur, categoryToDisplay)

        #Option 5: Quit the program
        if option == 5:
            break


#FR8
#Marks a task as complete or incomplete by toggling the completion status of the task
def markTask(conn, cur, taskToMark):
    #Uses SQL NOT operator to reverse the boolean value
    sql = """
    UPDATE Tasks
    SET completionStatus = NOT completionStatus
    WHERE taskID = %s
    """
    cur.execute(sql, (taskToMark, ))
    conn.commit()


#FR9
#Displays only the tasks that match a specific category that the user has entered  
def viewByCategory(cur, categoryToDisplay):
    sql = """
    SELECT *
    FROM Tasks
    WHERE category = %s
    """
    cur.execute(sql, (categoryToDisplay, ))
    rows = cur.fetchall()
    #Loops through and displays each result
    for row in rows:
        #Formats the output
        print(f"Task Number: {row[0]} | Task: {row[1]} | Category: {row[2]} | Due Date: {row[3]} | Completion Status:", ("Incomplete" if {row[4]} == 0 else "Complete"))
            

#FR10
#Checks if the input is blank, so prevents blank entries being added to the database
def isFieldBlank(input):
    #Returns True if the field is empty
    if not input:
        return True
    return False


#FR11
#Checks if the date entered matched the format YYYY-MM-DD
def isDateValid(date_string: str, fmt: str = "%Y-%m-%d") -> bool:
    try:
        #Attempts to convert the string to a datetime object
        datetime.strptime(date_string, fmt)
        return True
    #If the conversion fails then the format is incorrect
    except ValueError:
        return False
    

#Main
#Calls the function which runs the user interface
userInterface()


#Closes the database connection when the program ends
close_db(conn, cur)
print("Database connection closed.")