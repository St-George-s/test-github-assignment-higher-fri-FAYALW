# Simple scores linear search (a program to demonstrate a linear search)

# Creating an array called scores with 9 elements representing different scores
scores = [23, 45, 63, 99, 12, 27, 91, 50, 33]  
# Asking the user for input to search for a specific score and storing it in the variable search_value
search_value = int(input("Enter the value you are looking for: "))  
# Initializing a counter variable to track the current index being checked
counter = 0  
# Initializing a boolean variable called found to track if the search value has been found
found = False  

# Run the loop while the value has not been found and the counter is less than the length of the scores list
while found == False and counter != len(scores):  
    # Check if the score at the current index (counter) matches the search_value
    if scores[counter] == search_value:  
        found = True  # If the score matches, set found to True
    else:
        counter += 1  # If the score does not match, increment the counter to check the next index

# After the loop, check if the value was found
if found == True:
    # If found, print the position of the found value
    print("Your value was found at position " + str(counter))  
else:
    # If not found, inform the user that the value was not found
    print("Your value was not found")  
