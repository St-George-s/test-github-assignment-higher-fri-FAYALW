#In this code, the loop continues to ask for the password as long as the length of the password is less than 6 characters. Once a password of 6 or more characters is entered, the loop exits and "Password accepted" is printed
password = input("Enter your password: ")
while len(password) < 6:
    password = input("Password too short, please enter a password with at least 6 characters: ")
print("Password accepted")


#In this example, the loop keeps running as long as total_moneyis less than target_amount. Each iteration adds the user's input to the total. When the total reaches or exceeds 100, the loop stops and prints the total amount
total_money = 0
target_amount = 100
while total_money < target_amount:
    money = float(input("Enter an amount of money to add: "))
    total_money = total_money + money
print("Target reached. Total amount: + total_money")


#In many applications, while loops are used to control the flow of the program. For example, a menu-driven program might continue to display the menu and prompt for user input until the user selects the option to exit
choice = ""
while choice != "exit":
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("Type 'exit' to quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("You chose Option 1")
    elif choice == "2":
        print("You chose Option 2")
    elif choice != "exit":
        print("Invalid choice, try again.")
print("Program exited.")


# Question 1 Answer
code = input("Enter code: ")
while code != "rzy":
    code = input("Please re-enter code: ")
print("Code accepted")

# Question 2 Answer
code = int(input("Enter code: "))
while code != 4003:
    code = int(input("Please re-enter code: "))
print("Code accepted")

# Question 3 Answer
age = int(input("Enter your age: "))
while age <= 14:
    age = int(input("Age must be over 14, please re-enter your age: "))
print("Age accepted")

# Question 4 Answer
password = input("Enter password: ")
while len(password) <= 5:
    password = input("Password must be longer than 5 characters, please re-enter password: ")
print("Password accepted")

# Question 5 Answer
playAnother = input("Would you like to play another episode? ")
while playAnother == "yes":
    playAnother = input("Would you like to play another episode? ")
print("See you later!")

# Question 6 Answer
totalMoney = 0
while totalMoney <= 100:
    money = float(input("How much you got? "))
    totalMoney += money
print("I accept your offer")