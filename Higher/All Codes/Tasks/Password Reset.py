uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Creating a variable to hold all uppercase letters
lowercase = "abcdefghijklmnopqrstuvwxyz"  # Creating a variable to hold all lowercase letters
specialchar = "$@_"  # Creating a variable to hold special characters
digits = "0123456789"  # Creating a variable to hold all numerical digits

while True:  # Start an infinite loop to continuously prompt the user for a password
    lc = 0  # Initialize a counter for lowercase letters and set it to 0
    uc = 0  # Initialize a counter for uppercase letters and set it to 0
    user_password1 = input("Please enter your password: ")  # Prompt the user to enter a password and store it in user_password1
    user_password2 = input("Please enter your password again: ")  # Prompt the user to re-enter the password and store it in user_password2

    # Check if both passwords match and if the length of the first password is at least 8 characters
    if (user_password1 == user_password2) and len(user_password1) >= 8:  
        for i in user_password1:  # Iterate over each character in the first password
            if (i in lowercase):  # Check if the character is a lowercase letter
                lc += 1  # Increment the lowercase letter counter
            if (i in uppercase):  # Check if the character is an uppercase letter
                uc += 1  # Increment the uppercase letter counter
    
        # Assess the strength of the password based on the counts of lowercase and uppercase letters
        if lc < 2 and uc < 2:  # If there are less than 2 lowercase and uppercase letters
            print("Your password is weak.")  # Inform the user that the password is weak

        elif lc < 4 and uc < 4:  # If there are less than 4 lowercase and uppercase letters
            print("Your password is medium.")  # Inform the user that the password is medium

        else:  # If the password meets the strength criteria
            print("Your password is strong.")  # Inform the user that the password is strong
                
        # Check if there is at least one lowercase and one uppercase letter in the password
        if lc > 0 and uc > 0:  
            print("Your password has been updated.")  # Inform the user that the password has been updated
            break  # Exit the loop since a valid password has been entered

        else:  # If the password doesn't have the required complexity
            print("Your password is not complex enough. Please re-enter.")  # Ask the user to re-enter the password

    else:  # If the passwords do not match or the length requirement is not met
        print("Your passwords either don't match or are less than 8 characters.")  # Inform the user about the password requirements
