#Syntax
#random.randint(a, b)
#	• a: The lower limit of the range (inclusive).
#	• b: The upper limit of the range (inclusive).
	
#Let's say you want to simulate a dice roll, which means you want to generate a random number between 1 and 6:

import random

dice_roll = random.randint(1, 6)
print(dice_roll)