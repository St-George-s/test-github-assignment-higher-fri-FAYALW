# This for loop will print your name 10 times.
for i in range(10):
    print("Your Name")


# Ask for a number from the user
number = int(input("Enter a number for the times table: "))

# Calculate and print the times table for the entered number up to 12
for i in range(1, 13):
    # Concatenation of strings and type casting of integer to string
    print(str(number) + " x " + str(i) + " = " + str(number * i))


#In this example, += is used to update the total_age each time a new age is entered
total_age = 0
for i in range(10):
    age = int(input(f"Enter the age of person {i+1}: "))
    total_age += age  # Adds the age to the running total
print("The total age is: " + str(total_age))

# Exercise 1
# Loop will run 10 times and print the name each time
name = "Your Name"  # Replace with the actual name you wish to print
for x in range(10):
    print(name)

# Exercise 2
# Will ask for the user's name and then print it 1000 times
name = input("What is your name? ")
for x in range(1000):
    print(name)


# Exercise 3
# This will ask for the user's name and print a greeting followed by the name 1000 times
name = input("What is your name? ")
for x in range(1000):
    print("Hello " + name)

# Exercise 4
# This will print the 8 times table from 1 to 12
for number in range(1, 13):
    print("8 x " + str(number) + " = " + str(8 * number))

# Exercise 5
# Note: Printing the 8 times table up to 1000 would result in a very large output, so it's not practical to run this
# But this would be the code:
for number in range(1, 1001):
    print("8 x " + str(number) + " = " + str(8 * number))


# Exercise 6
# This will print the 7 times table from 1 to 12
for number in range(1, 13):
    print("7 x " + str(number) + " = " + str(7 * number))


# Exercise 7
# This will ask the user to input the age of 10 people and print each age
for i in range(1, 11):
    age = int(input("Enter the age of person " + str(i) + ": "))
    print("The age of person " + str(i) + " is: " + str(age))

# Exercise 8
# This will ask the user to input the age of 10 people and print each person's age in 10 years' time
for i in range(1, 11):
    age = int(input("Enter the age of person " + str(i) + ": "))
    print("The age of person " + str(i) + " in 10 years will be: " + str(age + 10))


# Exercise 9
# This will ask the user to input the age of 10 people, add up all the ages, and print the total
total_age = 0  # Initialize the total age to 0
for i in range(1, 11):  # Loop through the range for 10 people
    age = int(input("Enter the age of person " + str(i) + ": "))  # Get each person's age
    total_age += age  # Add each age to the running total
print("The total age is: " + str(total_age)) 