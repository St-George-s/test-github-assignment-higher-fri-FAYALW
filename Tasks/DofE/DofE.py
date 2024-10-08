import random

def generateUsername(firstName,lastName):
    firstName = firstName[:3]
    lastName = lastName[:3]
    randomNumber = random.randint(100,999)
    return firstName+lastName+str(randomNumber)

#main program
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")

username = generateUsername(firstName,lastName)
print(username)