# Prompt the user to choose a destination from the predefined options or enter their own
destination = input("Choose a destination: AES, SHA, OTP, or TLS or enter your own: ")

# Prompt the user to choose the type of ticket: Standard or First class
ticketType = input("Standard class or first class? ")

# Check the destination and ticket type to determine the ticket price
if destination == "AES" and ticketType == "Standard":
    # Calculate and print the ticket price for AES in Standard class
    print("£", round(106 * 0.925, 2), sep="")  # Price after discount
elif destination == "AES" and ticketType == "First":
    # Indicate that First class tickets for AES are unavailable
    print("Unavailable")

elif destination == "SHA" and ticketType == "Standard":
    # Calculate and print the ticket price for SHA in Standard class
    print("£", round(1000 * 0.85, 2), sep="")  # Price after discount
elif destination == "SHA" and ticketType == "First":
    # Calculate and print the ticket price for SHA in First class
    print("£", round(2200 * 0.7, 2), sep="")  # Price after discount

elif destination == "OTP" and ticketType == "Standard":
    # Calculate and print the ticket price for OTP in Standard class
    print("£", round(95 * 0.85, 2), sep="")  # Price after discount
elif destination == "OTP" and ticketType == "First":
    # Calculate and print the ticket price for OTP in First class
    print("£", round(190 * 0.7, 2), sep="")  # Price after discount

elif destination == "TLS" and ticketType == "Standard":
    # Calculate and print the ticket price for TLS in Standard class
    print("£", round(115 * 0.925, 2), sep="")  # Price after discount
elif destination == "TLS" and ticketType == "First":
    # Calculate and print the ticket price for TLS in First class
    print("£", round(210 * 0.9, 2), sep="")  # Price after discount

else:
    # If the destination is not one of the predefined options, prompt the user to enter the ticket price and distance
    ticketPrice = float(input("How much is your ticket?: "))
    miles = int(input("How far is your destination in miles?: "))

    # Calculate the price based on the miles and ticket type for distances up to 1000 miles
    if miles <= 1000 and ticketType == "Standard":
        print("£", round(ticketPrice * 0.925, 2), sep="")  # Price after discount for Standard
    elif miles <= 1000 and ticketType == "First":
        print("£", round(ticketPrice * 0.9, 2), sep="")  # Price after discount for First

    # Calculate the price based on the miles and ticket type for distances greater than 1000 miles
    elif miles > 1000 and ticketType == "Standard":
        print("£", round(ticketPrice * 0.85, 2), sep="")  # Price after discount for Standard
    elif miles > 1000 and ticketType == "First":
        print("£", round(ticketPrice * 0.7, 2), sep="")  # Price after discount for First
