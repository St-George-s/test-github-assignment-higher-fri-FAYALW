# Define character sets for password complexity requirements
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # String of uppercase letters
lowercase = "abcdefghijklmnopqrstuvwxyz"  # String of lowercase letters
specialchar = "$@_"  # String of special characters (not used in the current code)
digits = "0123456789"  # String of digits (not used in the current code)

# Start an infinite loop to prompt the user for password input
while True:
    lc = 0  # Initialize lowercase character count
    uc = 0  # Initialize uppercase character count
    # Prompt the user to enter their password twice for confirmation
    user_password1 = input("Please enter your password: ")
    user_password2 = input("Please enter your password again: ")

    # Check if the entered passwords match and if the first password is at least 8 characters long
    if (user_password1 == user_password2) and len(user_password1) >= 8:
        # Iterate through each character in the first password
        for i in user_password1:
            # Count lowercase characters
            if (i in lowercase):
                lc += 1
            # Count uppercase characters
            if (i in uppercase):
                uc += 1
    
        # Check password strength based on character counts
        if lc < 2 and uc < 2:
            print("Your password is weak.")  # Not enough lowercase and uppercase characters

        elif lc < 4 and uc < 4:
            print("Your password is medium.")  # Moderate number of lowercase and uppercase characters

        else:
            print("Your password is strong.")  # Sufficient number of lowercase and uppercase characters
                
        # Ensure that the password contains at least one lowercase and one uppercase character
        if lc > 0 and uc > 0:
            print("Your password has been updated.")  # Inform user that password is successfully updated
            break  # Exit the loop if the password meets all conditions

        else:
            print("Your password is not complex enough. Please re-enter.")  # Prompt user to re-enter password if complexity is insufficient

    else:
        print("Your passwords either don't match or are less than 8 characters. Please re-enter.")  # Inform user of validation failure
