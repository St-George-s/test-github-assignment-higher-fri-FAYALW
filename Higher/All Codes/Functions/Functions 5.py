# Function to calculate the sum of two numbers
def calc_val(num1, num2):
    total = 0  # Initialize a variable to store the sum
    total = num1 + num2  # Add num1 and num2 and assign the result to total
    return total  # Return the calculated total

# Function to calculate the product of two numbers
def mult_val(num1, num2):
    mult = 0  # Initialize a variable to store the product
    mult = num1 * num2  # Multiply num1 and num2 and assign the result to mult
    return mult  # Return the calculated product

# Prompt the user to enter the first number and convert it to an integer
num1 = int(input("enter number 1: "))

# Prompt the user to enter the second number and convert it to an integer
num2 = int(input("enter number 2: "))

# Call the calc_val function to get the sum of num1 and num2
total = calc_val(num1, num2)

# Call the mult_val function to get the product of num1 and num2
mult = mult_val(num1, num2)

# Print the result of the addition
print("Sum:", total)

# Print the result of the multiplication
print("Product:", mult)
