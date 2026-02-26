# Finds out the circumference of a circle given the radius

# The following lines are commented out as they were used for testing purposes
# myRadius = ""  # Initialize myRadius as an empty string
# myRadius = (input("Enter a circle's radius value and I will calculate its circumference: "))  # Prompt user for radius input
# print(myRadius)  # Print the input value
# print(type(myRadius))  # Print the type of the input value (should be str)
# print(isinstance(myRadius, int))  # Check if myRadius is an integer (will be False)

while True:  # Start an infinite loop to repeatedly ask for input until valid
    try:
        # Prompt the user to enter the radius of the circle
        myRadius = input("Please enter a circle's radius and I will calculate its circumference: ")
        myRadius = int(myRadius)  # Attempt to convert the input to an integer
        break  # Exit the loop if conversion is successful
    except ValueError:  # Handle the case where conversion fails
        # Inform the user that the input was not a number and prompt to try again
        print(myRadius, "is not a number! Please try again. shtatahshteeninty?? shinoohathalhachi?????: ")

# Calculate and print the circumference of the circle using the formula: circumference = 2 * π * radius
print(2 * 3.14 * myRadius)  # Using 3.14 as an approximation for π
