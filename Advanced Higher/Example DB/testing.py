#Showing a specific task
# def showSpecificTask(cur):
#     sql = """
#     SELECT taskID,
#            taskName,
#            category,
#            dueDate,
#            completionStatus
#     FROM Tasks
#     WHERE taskID = %s AND category = %s;
#     """
#     cur.execute(sql, (3,"Household"))
#     rows = cur.fetchall()
#     print(rows)


# from datetime import datetime 

# def isDateValid(date_string: str, fmt: str = "%Y-%m-%d") -> bool:
#     try:
#         datetime.strptime(date_string, fmt)
#         return True
#     except ValueError:
#         return False

# print(isDateValid("1985-13-22"))
# print(isDateValid("2034-12-22"))
# print(isDateValid("2027-02-28"))


# def isFieldBlank(input):
#     if not input:
#         print("Please enter something: ")

# isFieldBlank("he")