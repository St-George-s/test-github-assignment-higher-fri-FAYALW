# Get the current day from the user
day = input("What day is it today?: ")
# Get the current time as a float from the user
time = float(input("What is the time?: "))

# Check if today is Monday and the time is in the morning (6 AM to 12 PM)
if day == "Monday" and time >= 6.00 and time < 12.00:
    print("You should be doing Computer Science")  # Suggest Computer Science class
# Check if today is Monday and the time is in the afternoon (12 PM to 6 PM)
elif day == "Monday" and time >= 12.00 and time < 18.00:
    print("You are free!")  # Indicate the user is free

# Check if today is Tuesday and the time is in the morning (6 AM to 12 PM)
if day == "Tuesday" and time >= 6.00 and time < 12.00:
    print("You should be doing Maths")  # Suggest Maths class
# Check if today is Tuesday and the time is in the afternoon (12 PM to 6 PM)
elif day == "Tuesday" and time >= 12.00 and time < 18.00:
    print("You should be doing Science")  # Suggest Science class

# Check if today is Wednesday and the time is in the morning (6 AM to 12 PM)
if day == "Wednesday" and time >= 6.00 and time < 12.00:
    print("You are free!")  # Indicate the user is free
# Check if today is Wednesday and the time is in the afternoon (12 PM to 6 PM)
elif day == "Wednesday" and time >= 12.00 and time < 18.00:
    print("You should be doing English")  # Suggest English class

# Check if today is Thursday
if day == "Thursday":
    print("You should be doing Computer Science. Study if statements.")  # Suggest studying Computer Science

# Check if today is Friday and the time is in the morning (6 AM to 12 PM)
if day == "Friday" and time >= 6.00 and time < 12.00:
    print("You should be doing Music")  # Suggest Music class
# Check if today is Friday and the time is in the afternoon (12 PM to 6 PM)
elif day == "Friday" and time >= 12.00 and time < 18.00:
    print("You are free!")  # Indicate the user is free
