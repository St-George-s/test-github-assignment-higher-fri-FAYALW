# Prompt the user to input their first name
firstName = input("What is your first name?")

# Prompt the user to input their surname
surName = input("What is your surname?")

# Ask the user to specify their position: 'S' for student, 'T' for teacher
position = input("If you are a student, input S, and if you are a teacher, input T: ")

# Check if the user is a teacher
if position == "T":
    # If the user is a teacher, create a username using the last three letters of the surname
    # and the first two letters of the first name
    username = surName[-3:] + firstName[:2]
else:
    # If the user is a student, create a username using the first three letters of the first name
    # and the first two letters of the surname
    username = firstName[:3] + surName[:2]

# Print the generated username
print(username)
