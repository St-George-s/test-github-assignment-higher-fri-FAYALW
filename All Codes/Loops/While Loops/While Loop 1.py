# Initialize the counter variable to 0
counter = 0  
# Initialize input_string variable to hold user input
input_string = 0  

# Loop until the user enters 'x'
while input_string != 'x':
    # Print the current value of the counter
    print("counter value is ", counter)  
    # Prompt the user to enter a word
    input_string = input('Please enter a word')  
    # Increment the counter by 1 for each valid input
    counter += 1  

# Once the loop ends (user enters 'x'), print the final counter value
else:
    print ('The final counter value is ', counter)  
