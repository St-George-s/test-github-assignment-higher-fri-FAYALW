# Define a 2-D array (table)
table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(table[0][0])  # Outputs: 1
print(table[1][2])  # Outputs: 6
print(table[2][1])  # Outputs: 8

# Iterating through the 2-D array
for row in table:
    for element in row:
        print(element, end=' ')
    print()  # New line after each row