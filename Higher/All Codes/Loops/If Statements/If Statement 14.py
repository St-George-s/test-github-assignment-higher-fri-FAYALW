# Adds together 3 amounts and multiplies by 2 if the total is more than or equal to 1000

# Prompt the user to enter the first amount of money
amount1 = int(input("enter your first amount")) 

# Prompt the user to enter the second amount of money
amount2 = int(input("enter your second amount")) 

# Prompt the user to enter the third amount of money
amount3 = int(input("enter your third amount")) 

# Calculate the total by adding the three amounts together
total = amount1 + amount2 + amount3 

# Check if the total is greater than or equal to 1000
if total >= 1000:  
    total = total * 2  # If true, double the total amount
    print(total)  # Print the updated total

else: 
    print(total)  # If false, print the original total
