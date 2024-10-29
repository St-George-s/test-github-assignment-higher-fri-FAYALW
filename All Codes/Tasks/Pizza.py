# Welcome message for the pizza ordering system
print("Welcome to Geidi Prime Pizza.")

while True:
    # Prompt the user to enter their mobile number
    mobileNumber = input("Please enter your mobile number: ")

    # Check if the number starts with +971 (the country code for the UAE)
    # If it does, remove the country code for now
    if mobileNumber[0:4] == "+971":
        mobileNumber = mobileNumber[4:]

    # Check if the number starts with 0 (local format)
    # If it does, remove the leading zero for now
    elif mobileNumber[0:1] == "0":
        mobileNumber = mobileNumber[1:]

    # Remove any spaces from the mobile number
    mobileNumber = mobileNumber.replace(" ","")

    # Check if the length of the mobile number is 9 and all characters are digits
    if len(mobileNumber) == 9 and mobileNumber.isdigit():
        break  # If valid, exit the loop

    # If the number is invalid, inform the user and loop again
    else:
        print("Mobile number entered is invalid. Please try again: ")

# Confirmation message for the accepted mobile number
print("Mobile number accepted, thank you!")

# Add the +971 country code back to the mobile number for proper formatting
mobileNumber = "+971" + mobileNumber
print(mobileNumber)  # Display the final mobile number
