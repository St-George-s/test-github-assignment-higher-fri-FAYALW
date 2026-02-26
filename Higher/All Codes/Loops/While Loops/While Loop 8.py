# Adds together prices until the subtotal reaches or exceeds 150

sub_tot = 0  # Initialize the subtotal to 0
get_price = 0  # Initialize the price variable to store user input

# Continue looping while the subtotal is less than 150
while sub_tot < 150:  # Check if the running total is under 150
    get_price = int(input("please enter a price "))  # Prompt the user to enter a price and convert it to an integer
    sub_tot = get_price + sub_tot  # Add the entered price to the current subtotal
    # Display the current subtotal after adding the new price
    print("the subtotal currently is £" + str(sub_tot))  # Print the current subtotal in pounds

# Once the loop condition is no longer met (subtotal is 150 or more)
print(sub_tot)  # Print the final subtotal (the loop stops when the total is at least 150)
