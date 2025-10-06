# Finds out circumference of a circle given the radius

print("enter radius value")  # Asks the user to input a radius value

myRadius = ""  # Initializes a variable myRadius to store the radius value
myRadius = int(input())  # Converts the user input to an integer and assigns it to myRadius

# Calculates the circumference of the circle using the formula: circumference = 2 * π * radius
# Here, π is approximated as 3.14
print(2 * 3.14 * myRadius)  # Outputs the calculated circumference to the user