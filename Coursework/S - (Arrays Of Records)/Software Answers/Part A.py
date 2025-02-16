# Import the csv module to handle reading data from CSV files
import csv

# Define an Order class to store order details
class Order():
    def __init__(self, customerName, productPurchased, amountSpent):
        # Initialize attributes for each order
        self.customerName = customerName        # Customer's name
        self.productPurchased = productPurchased  # Product name
        self.amountSpent = amountSpent          # Amount spent on the product

# Function to read orders from the CSV file and create Order objects
def readOrdersFromCSV():
    orders = []  # Initialize an empty list to store Order objects

    # Open the CSV file containing order data
    with open('Mock Class Test/orders.csv', 'r') as file:
        reader = csv.reader(file)  # Create a CSV reader to process each row
        header = next(reader)      # Skip the header row

        # Loop over each row in the CSV file and create an Order object
        for row in reader:
            newOrder = Order(
                row[0],            # Customer name from first column
                row[1],            # Product purchased from second column
                float(row[2])      # Amount spent from third column, converted to float
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

# Main Program
# Read orders from CSV and store them in the orders list
orders = readOrdersFromCSV()

# Find and display the highest order amount for a product containing "TV"
findMaxOrderWithTV(orders)