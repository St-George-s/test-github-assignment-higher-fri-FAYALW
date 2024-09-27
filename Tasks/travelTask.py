import sys

def get_destination():
    destination = input("Enter your travel destination: ")
    if destination == "End":
        print_travel_details(allTravel)
        sys.exit("You have chosen to quit this program.")
    else:
        return destination
    
def get_number_of_people():
    return input("Enter the number of people: ")

def get_travel_method():
    return input("Enter your travel method: ")

def print_travel_details(allTravel):
    print("All travel list: ", allTravel)
 
##main
localDestinations = ["Edinburgh", "Glasgow", "Dundee", "Aberdeen"]

##The main list to hold all travel information
global allTravel
allTravel = []
 
##The temporary list to hold travel information for each round only
latestTravel = []
 
while True:
##Call the different functions to get the travel information and add each value to the temporary list
    latestDest=get_destination()
    latestTravel.append(latestDest)

    if latestDest not in localDestinations:
        latestPeop=get_number_of_people()
        latestTravel.append(latestPeop)
     
        latestMeth=get_travel_method()
        latestTravel.append(latestMeth)

    else:
        latestPeop=get_number_of_people()
        latestTravel.append(latestPeop)
        
        latestMeth = "Local transport"
        latestTravel.append(latestMeth)
 
    ##Add the temporary list to the main list which holds all travel information
    allTravel.append(latestTravel.copy())
    #print_travel_details(allTravel)
 
    ##Clear the temporary travel list so we don't get duplicates
    latestTravel.clear()