rows = 5  # Set the number of rows for the pattern

# Outer loop to control the number of rows
for a in range(rows, 0, -1):  # Loop from 'rows' down to 1
    # print("a is equal to:", a)  # Uncomment for debugging: shows current row number
    # Inner loop to control the number of asterisks per row
    for b in range(a, 0, -1):  # Loop from the current row number 'a' down to 1
        # print("b is equal to:", b)  # Uncomment for debugging: shows current asterisk count
        print("*", end=" ")  # Print an asterisk without a newline, followed by a space
    print()  # Move to the next line after printing all asterisks for the current row
