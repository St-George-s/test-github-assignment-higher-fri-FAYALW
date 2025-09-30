# Asks for 3 amounts of collected charity money and checks if the total is eligible for doubling

# Prompt user for the first amount raised and convert it to an integer
one = int(input("enter the first amount raised: "))  

# Prompt user for the second amount raised and convert it to an integer
two = int(input("enter the second amount raised: "))  

# Prompt user for the third amount raised and convert it to an integer
three = int(input("enter the third amount raised: "))  

# Calculate total collection by adding the three amounts
totalcollection = one + two + three  

# Print the total amount raised
print("you raised " + str(totalcollection))  

# Check if the total collection is greater than or equal to 1000
if totalcollection >= 1000:  
    # If it is, double the total and print the new amount
    print("your money has been doubled to " + str(totalcollection * 2))  
else:  
    # If it is less than 1000, inform the user that the amount is insufficient for doubling
    print("you didn't raise enough money for it to be doubled!")  
