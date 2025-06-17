# Import the csv module to handle reading data from CSV files
import csv

# Define an Order class to store detailed order information
class Order():
    def __init__(self, customerID, customerName, productPurchased, amountSpent, category):
        # Initialize attributes for each order
        self.customerID = customerID            # Unique identifier for the customer
        self.customerName = customerName        # Name of the customer
        self.productPurchased = productPurchased  # Name of the product purchased
        self.amountSpent = amountSpent          # Amount of money spent on the product
        self.category = category                # Category of the purchased product

# Function to read orders from the CSV file and create Order objects
def readOrdersFromCSV():
    orders = []  # Initialize an empty list to store Order objects

    # Open the CSV file containing extended order data
    with open('Mock Class Test/ordersExtended.csv', 'r') as file:
        reader = csv.reader(file)  # Create a CSV reader to process each row
        header = next(reader)      # Skip the header row

        # Loop over each row in the CSV file and create an Order object
        for row in reader:
            newOrder = Order(
                row[0],            # Customer ID from first column
                row[1],            # Customer name from second column
                row[2],            # Product purchased from third column
                float(row[3]),     # Amount spent from fourth column, converted to float
                row[4]             # Category from fifth column
            )
            # Append the new Order object to the orders list
            orders.append(newOrder)

    # Return the list of Order objects
    return orders

# Function to find the order with the highest amount spent on any product containing "TV"
def findMaxOrderWithTV(orders):
    maxOrder = orders[0]  # Initialize with the first order in the list

    # Loop through all orders to find the highest amount spent on "TV" products
    for order in orders:
        # Check if "TV" is in the product name and if the amount spent is greater than current max
        if "TV" in order.productPurchased and order.amountSpent > maxOrder.amountSpent:
            maxOrder = order  # Update maxOrder if a higher amount is found for a "TV" product

    # Print the product and amount spent for the order with the highest "TV" purchase
    print(maxOrder.productPurchased, maxOrder.amountSpent)

# Function to assign discount codes based on customer ID and write the results to a text file
def discount(orders):
    # Open a text file to write discount information
    with open('textFile.txt', 'w') as file:
        # Loop through all orders to check for discount eligibility
        for order in orders:
            # Check if the customer ID is divisible by 5
            if int(order.customerID) % 5 == 0:
                # Write discount code assignment to the file for eligible orders
                file.write(order.customerID + "-" + order.productPurchased[:3] + "-DISCOUNT CODE ASSIGNED" + "\n")
            else:
                # Write no discount message for ineligible orders
                file.write(order.customerID + "-" + order.productPurchased[:3] + "-NO DISCOUNT" + "\n")

# Main Program
# Read orders from CSV and store them in the orders list
orders = readOrdersFromCSV()

# Find and display the highest order amount for a product containing "TV"
findMaxOrderWithTV(orders)

# Process discount eligibility and write results to the text file
discount(orders)