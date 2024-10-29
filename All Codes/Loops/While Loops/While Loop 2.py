# Initialize the counter variable to 0
counter = 0  
# Initialize input_string to an empty string
input_string = ''  

# Prompt the user to enter a word and store it in input_string
input_string = input("enter a word")  
# Print a message to prompt the user (this line will print again after the input)
print("enter a word")  

# Check if the user entered 'x'
if input_string == 'x':
    # If 'x' is entered, print the current value of counter
    print(counter)  
else:
    # If any other word is entered, increment the counter by 1
    counter += 1  

# The following code is commented out. It seems to be an alternative loop approach:
# while input_string != 'x':
#     print("enter a word")  # Print a message to prompt the user for input
#     counter += 1  # Increment the counter for each valid word entered
# else:
#     print(counter)  # Print the final counter value when 'x' is entered
