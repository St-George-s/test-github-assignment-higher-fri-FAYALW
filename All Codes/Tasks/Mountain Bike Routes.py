# Define the correct email address and password
emailAddress = "tariq@azmail.co.uk"  # Correct email for authentication
password = "P_5*Kl@8"                 # Correct password for authentication
attempt = 0                            # Initialize the number of attempts made

# Allow the user up to 4 attempts to enter the correct email and password
while attempt < 4:  # Loop until the user has made 4 attempts
    # Prompt the user to enter their email and password
    userEmail = input("Please enter your email address: ")  
    userPassword = input("Please enter your password: ")
    
    # Increment the attempt counter
    attempt = attempt + 1

    # Check if the entered email and password match the correct credentials
    if userEmail == emailAddress and userPassword == password:
        print("Welcome")  # If credentials are correct, welcome the user
        break  # Exit the loop since the user has successfully logged in
    else:
        print("Incorrect")  # Inform the user that the credentials are incorrect

# This else block is associated with the while loop, not the if statement
else:
    print("You are out of attempts")  # Inform the user that they have used all attempts
