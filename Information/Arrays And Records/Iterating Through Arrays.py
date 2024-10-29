#Indexing in Arrays
#Indexing allows you to access individual elements in an array using their position. The first element has an index of 0, the second element has an index of 1, and so on.

numbers = [10, 20, 30, 40, 50]

# Access the first element
first_element = numbers[0]
print(first_element)  # Output: 10

# Access the last element
last_element = numbers[-1]
print(last_element)  # Output: 50

# Access the third element
third_element = numbers[2]
print(third_element)  # Output: 30

#Iterating Through Arrays
#You can iterate through arrays using loops to access and manipulate each element.

#Using a for Loop
#A for loop is commonly used to iterate through each element in an array.

names = ["Alice", "Bob", "Charlie"]
# Iterate through the array and print each element
for name in names:
    print(name)
# Output:
# Alice
# Bob
# Charlie

#Using a for Loop with Index
#You can also use a for loop to access both the elements and their indices.

names = ["Alice", "Bob", "Charlie"]
# Iterate through the array using the range function to access indices
for i in range(len(names)):
    print(f"Index {i} has value {names[i]}")
# Output:
# Index 0 has value Alice
# Index 1 has value Bob
# Index 2 has value Charlie


#Using a while Loop
#A while loop can be used to iterate through an array until a certain condition is met.

numbers = [1, 2, 3, 4, 5]
i = 0
# Iterate through the array using a while loop
while i < len(numbers):
    print(numbers[i])
    i += 1
# Output:
# 1
# 2
# 3
# 4
# 5

#Modifying Elements in Arrays
#You can change the elements in an array by accessing them through their index.

numbers = [10, 20, 30, 40, 50]
# Modify the second element
numbers[1] = 25
print(numbers)  # Output: [10, 25, 30, 40, 50]
# Modify the last element
numbers[-1] = 60
print(numbers)  # Output: [10, 25, 30, 40, 60]