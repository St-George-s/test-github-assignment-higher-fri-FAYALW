import csv # Import the csv module to handle reading data from CSV files

class Order(): #Defines an Order class to store detailed order information
    def __init__(self, orderNum, date, email, option, cost, rating):
        self.orderNum = orderNum #Initializes attributes for each order
        self.date = date   
        self.email = email  
        self.option = option      
        self.cost = cost
        self.rating = rating                


def readOrdersFromCSV(): #Defines a function to read the data from the CSV file
    with open('Coursework 2025/orders.txt', 'r') as file: #Opens the file
        reader = csv.reader(file) # Creates a CSV reader to process each row
        orders = [] #Creates an array to store the data called orders
        for row in reader: #Loops over each row in the CSV file and create an Order object
            newOrder = Order(
                row[0], #orderNum from first column           
                row[1], #date from second column  
                row[2], #email from third column          
                row[3], #option from fourth column   
                float(row[4]), #cost from fifth column converted to a float
                int(row[5]) #rating from sixth column converted to an integer       
            )
            orders.append(newOrder) #Appends the new Order object to the orders array
    return orders #Returns the array


def findPosition(orders): #Defiunes a function to find the position of the customer who gave the first 5-star rating of the month
    position = -1 #Creates a variable called position and sets it to -1
    index = 0 #Creates a variable called index and sets it to 0
    monthToSearch = input("Enter the first three letters of the month to search: ") #Takes an input (name of month) from the user and assigns their input to the variable monthToSearch
    for order in orders: #Loops through every record in the array
        while position == -1 and index < len(orders): #While loop to check if the position is -1 (haven't found the winner yet) and the index is less than the length of the array (hasn't reached the end of the array yet)
            if monthToSearch in orders[index].date and orders[index].rating == 5: # If statement to check if the user input is found in the current month and if the current rating is 5
                position = index #Sets position to index
            index += 1 #Adds 1 to index
    return position #Returns the position


def writeDetailsToFile(orders, position): #Defines a procedure to write the details to a text file
    with open('Coursework 2025/winningCustomer.txt', 'w') as file: #Opens a new file
            if position >= 0: #If statement to check if the position is above or equal to 0 because if it is not above or equal to 0 then that means that there was no 5-star rating for that month
                file.write(str(orders[position].orderNum) + "," + str(orders[position].email) + "," + str(orders[position].cost)) #If the position is above or equal to 0 then it writes the order number, email, and cost that were at the position to the file
            else: #Else
                file.write('No winner') #If the position is not above or equal to 0 it writes 'No winner' to the file as it means no one gave a 5-star rating for that month so there is no winning customer


def countOption(orders, option): #Defines a function to count the number of orders delivered and collected
    count = 0 #Creates a variable called counter and sets it to 0
    for counter in range(len(orders)):
        if orders[counter].option == option:
            count += 1
    return count

#Main program
mainOrders = readOrdersFromCSV()

mainPosition = findPosition(mainOrders)

writeDetailsToFile(mainOrders, mainPosition)

deliveryTotal = countOption(mainOrders, "Delivery")
collectionTotal = countOption(mainOrders, "Collection")

print(deliveryTotal)
print(collectionTotal)