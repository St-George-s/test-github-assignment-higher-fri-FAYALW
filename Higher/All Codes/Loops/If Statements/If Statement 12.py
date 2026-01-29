# Initialize counters for present and absent students
present = 0  # Counter for the number of students marked as present
absent = 0   # Counter for the number of students marked as absent

# Creates an array called studentnames containing the names of students
studentnames = ["Emily"]  # You can add more names to this list if needed

# Iterate through the list of student names
for i in range(len(studentnames)):  # Loop from 0 to the length of studentnames - 1
    print(studentnames[i])  # Print the current student's name
    
    # Ask for attendance status input from the user
    attendance = input("absent or present? ")  # Prompt the user to enter attendance status
    
    # Check if the attendance input is "present"
    if attendance == "present":
        present += 1  # Increment the present counter if the student is present
    else:
        absent += 1  # Increment the absent counter if the student is absent

# Print the total number of present and absent students
print("Present students: " + str(present))  # Display the number of students present
print("Absent students: " + str(absent))    # Display the number of students absent

# Reset counters for future use (if necessary)
present = 0  # Reset the present counter
absent = 0   # Reset the absent counter