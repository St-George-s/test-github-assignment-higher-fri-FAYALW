import csv # Import the CSV module to handle reading data from CSV files

class Order(): #Defines an Order class to store detailed order information
    def __init__(self, orderNum, date, email, option, cost, rating): #Initialises the categories in the record
        self.orderNum = orderNum #Initialises attributes for each order
        self.date = date   
        self.email = email  
        self.option = option      
        self.cost = cost
        self.rating = rating                


def readOrdersFromFile(): #Defines a function to read the data from the file and store it in an array of records
    with open('Coursework 2025/orders.txt', 'r') as file: #Opens the file
        reader = csv.reader(file) # Creates a CSV reader to process each row and reads the file
        orders = [] #Creates an array called orders to store the data from the file
        for row in reader: #Loops over each row in the file and create an Order object
            newOrder = Order( #For each order/row in the file it makes a new record
                row[0], #Gets each category from each column      
                row[1],   
                row[2],         
                row[3],
                float(row[4]), 
                int(row[5])
            )
            orders.append(newOrder) #Appends each new order to the orders array
    return orders #Returns the array


def findPosition(orders): #Defines a function to find the position of the customer who gave the first 5-star rating of the month
    position = -1 #Creates a variable called position and sets it to -1
    index = 0 #Creates a variable called index and sets it to 0
    monthToSearch = input("Enter the first three letters of the month to search: ") #Takes an input (name of month) from the user and assigns their input to the variable monthToSearch
    while position == -1 and index < len(orders): #While loop to check if the position is -1 (meaning the winner hasn't been found yet) and the index is less than the length of the array (meaning the end of the array has not been reached yet)
        if orders[index].date[3:6] == monthToSearch and orders[index].rating == 5: #If statement to check if the user input is found in the current month and if the current rating is 5
            position = index #Sets position to index
        index += 1 #Adds 1 to index
    return position #Returns the position


def writeDetailsToFile(orders, position): #Defines a procedure to write the details to a text file
    with open('Coursework 2025/winningCustomer.txt', 'w') as file: #Opens a new file
        if position >= 0: #If statement to check if the position is above or equal to 0 because if it is not above or equal to 0 then that means that there was no 5-star rating for that month
            file.write(str(orders[position].orderNum) + "," + str(orders[position].email) + "," + str(orders[position].cost)) #If the position is above or equal to 0 then it writes the corresponding order number, email, and cost of the customer who was at that position
        else:
            file.write('No winner') #If the position is not above or equal to 0 it writes 'No winner' to the file as it means no one gave a 5-star rating for that month so there is no winning customer


def countOption(orders, option): #Defines a function to count the number of orders delivered and collected
    count = 0 #Creates a variable called count and sets it to 0
    for counter in range(len(orders)): #Goes through the array using the length of the orders array as the amount of times to loop through
        if orders[counter].option == option: #Checks if the current option is equal to the option that will be specified by being passed in to the function in the main program ('Delivery' or 'Collection)
            count += 1 #Adds one to count if the condition is true
    return count #Returns the count


def displayTotals(orders): #Defines a procedure to display the total number of orders delivered and collected
    deliveryTotal = countOption(orders, "Delivery") #Calls the countOption function, passing in 'Delivery' as the option so that it counts the number of deliveries and assigns the value to the variable deliveryCount
    collectionTotal = countOption(orders, "Collection") #Calls the countOption function, passing in 'Collection' as the option so that it counts the number of collection and assigns the value to the variable collectionCount
    print("Total number of orders delivered to date:", deliveryTotal) #Prints the total number of orders delivered
    print("Total number of orders collected to date:", collectionTotal) #Prints the total number of orders collected


#Main program
orders = readOrdersFromFile() #Calls the function which reads the data from the file and stores it in an array of records

position = findPosition(orders) #Calls the function which finds the position of the winning customer and assigns the value to the variable position

writeDetailsToFile(orders, position) #Calls the procedure which writes the details of the customer who won or writes that there was no winner to a file

displayTotals(orders) #Calls the procedure which outputs the total number of orders delivered and collected