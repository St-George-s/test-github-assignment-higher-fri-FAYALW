# Initialize empty sets to hold different categories of numbers
oddNumbers = set()  # To store all odd numbers
mults13 = set()     # To store multiples of 13
mults16 = set()     # To store multiples of 16
perfNumbers = set() # To store perfect numbers

# Generate odd numbers from 1 to 10,000
for x in range(1, 10001, 2):  # Start at 1, go up to 10,000, increment by 2
    oddNumbers.add(x)  # Add each odd number to the set

# Generate multiples of 13 from 0 to 10,000
for x in range(0, 10001, 13):  # Start at 0, go up to 10,000, increment by 13
    mults13.add(x)  # Add each multiple of 13 to the set

# Generate multiples of 16 from 0 to 10,000
for x in range(0, 10001, 16):  # Start at 0, go up to 10,000, increment by 16
    mults16.add(x)  # Add each multiple of 16 to the set

# Initialize the set with the known perfect number 6
perfNumbers = {6}  
# Check for perfect numbers from 1 to 10,000
for i in range(1, 10001):  # Loop through each number from 1 to 10,000
    total = 0  # Initialize total to sum the factors of i
    # Check all numbers from 1 up to but not including i
    for j in range(1, i):  # Loop through potential factors
        # See if this number (j) is a factor of i
        if i % j == 0:  # If j divides i evenly
            total += j  # Add j to total
    # Once all factors have been added, see if this total equals i
    if total == i:  # If the sum of factors equals the number itself
        # If it does, i must be perfect
        perfNumbers.add(i)  # Add the perfect number to the set

# Print all perfect numbers found in the range
print("The perfect numbers in this range are:", perfNumbers)

# Find and print the first 10 odd multiples of 13
print("10 numbers which are multiples of 13 and also odd are:")
mults13OddNumbers = list(mults13 & oddNumbers)  # Intersection of odd numbers and multiples of 13
for x in range(10):  # Loop to print the first 10 numbers
    print(mults13OddNumbers[x])  # Print each number

# Print multiples of 13 which are not odd numbers
print("The multiples of 13 which are not odd numbers are:", mults13 - oddNumbers)

# Print numbers which are perfect and multiples of 16
print("The numbers which are perfect and multiples of 16 are:", mults16 & perfNumbers)  # Intersection of perfect numbers and multiples of 16
