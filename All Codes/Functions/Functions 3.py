# Function to add two numbers
def add_val(num1, num2):
    # Initialize the result variable
    add = 0
    # Calculate the sum of num1 and num2
    add = num1 + num2
    # Return the result of the addition
    return add

# Function to multiply two numbers
def mult_val(num1, num2):
    # Initialize the result variable
    mult = 0
    # Calculate the product of num1 and num2
    mult = num1 * num2
    # Return the result of the multiplication
    return mult

# Function to divide two numbers
def div_val(num1, num2):
    # Initialize the result variable
    div = 0
    # Calculate the division of num1 by num2
    div = num1 / num2
    # Return the result of the division
    return div

# Function to subtract one number from another
def sub_val(num1, num2):
    # Initialize the result variable
    sub = 0
    # Calculate the difference between num1 and num2
    sub = num1 - num2
    # Return the result of the subtraction
    return sub

# Prompt the user to enter the first number and convert it to an integer
num1 = int(input("Enter number 1: "))
# Prompt the user to enter the second number and convert it to an integer
num2 = int(input("Enter number 2: "))

# Call each function with num1 and num2 as arguments and store the results
add = add_val(num1, num2)
mult = mult_val(num1, num2)
div = div_val(num1, num2)
sub = sub_val(num1, num2)

# Print the results of each arithmetic operation
print(add)
print(mult)
print(div)
print(sub)