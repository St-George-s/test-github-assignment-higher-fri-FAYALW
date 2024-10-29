# Initialize a list of names
name = ['Gabriella', 'Ariana', 'Jenna']  
# Initialize a corresponding list of phone numbers
number = ['1352678403', '5748392017', '7126789034']  

# Prompt the user to enter their name and store it in the variable get_name
get_name = input("Please enter your name: ")  
# Append the entered name to the name list
name.append(get_name)  

# Prompt the user to enter their phone number and store it in the variable get_number
get_number = input("Please enter your number: ")  
# Append the entered number to the number list
number.append(get_number)  

# Check if the entered name and number do not match any in the lists
if get_number not in number or get_name not in name:  
    # If neither the name nor the number exists in their respective lists, print a message
    print('The contact was not found')  
else:
    # If the name and number are found, print the entered name and number
    print(get_name, get_number)  
