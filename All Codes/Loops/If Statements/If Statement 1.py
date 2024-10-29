# Asks for the user's name and checks if it exceeds 10 characters

# Prompt the user to input their name
name = input("what is your name?") 

# Calculate the length of the entered name
len_name = len(name)

# Check if the length of the name is greater than 10 characters
if len_name > 10: 
    # If the name has more than 10 characters, print 'NO'
    print("NO") 
else: 
    # If the name has 10 characters or fewer, print 'YES'
    print("YES") 
