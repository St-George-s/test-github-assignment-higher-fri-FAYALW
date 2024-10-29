# Define character sets for password complexity requirements
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # String of uppercase letters
lowercase = "abcdefghijklmnopqrstuvwxyz"  # String of lowercase letters
specialchar = "$@_"  # String of special characters
digits = "0123456789"  # String of digits
lc = 0  # Initialize lowercase character count
uc = 0  # Initialize uppercase character count

while True:  # Start an infinite loop to prompt for password input
    user_password1 = input("Please enter your password: ")  # Prompt user for the first password
    user_password2 = input("Please enter your password again: ")  # Prompt user for password confirmation

    # Check if both passwords match and the first password is at least 8 characters long
    if (user_password1 == user_password2) and len(user_password1) >= 8:
        print("Passwords match and are longer than 8 characters.")  # Inform the user of success
        # Loop through each character in the first password to count character types
        for i in user_password1:
            print("Inside the 'for loop'")  # Indicate that the loop is being executed
            if (i in lowercase):  # Check if the character is lowercase
                lc += 1  # Increment lowercase character count
            if (i in uppercase):  # Check if the character is uppercase
                uc += 1  # Increment uppercase character count
            # Print current counts of lowercase and uppercase characters
            print("The lc count is", lc)  # Show the count of lowercase characters
            print("The uc count is", uc)  # Show the count of uppercase characters

        # Check if there are no lowercase or uppercase characters
        if lc == 0 or uc == 0:
            print("Your password is not complex enough. Please enter again")  # Notify user about password complexity
            continue  # Restart the loop to prompt for password again

        break  # Exit the loop if the password is valid and complex enough

    else:
        print("Your passwords don't match or are not long enough")  # Notify user of invalid password input

print("Your password has met the requirements and has been updated")  # Confirm password update
