# List of accounts, each represented as a dictionary containing name, pin, and balance
accounts = [
    {"name": "Alice", "pin": "1234", "balance": 1000.0},
    {"name": "Bob", "pin": "5678", "balance": 1500.0},
    {"name": "Eve", "pin": "9876", "balance": 2000.0}
]

def main():
    # Prompt user to enter their name
    name = input("Enter your name: ")
    # Prompt user to enter their PIN
    pin = input("Enter your PIN: ")
    # Prompt user to enter their bank balance and convert it to float
    balance = float(input("Enter your bank balance: "))
    
    # Initialize a flag to check if the account matches
    account_matched = False
    
    # Iterate through the list of accounts to check for a match
    for account in accounts:
        # Check if the entered name, pin, and balance match an account
        if account["name"] == name and account["pin"] == pin and account["balance"] == balance:
            account_matched = True  # Set flag to True if match is found
            break  # Exit loop as the account is found
    
    # Print authentication result based on the account matching status
    if account_matched:
        print("Authentication successful.")
    else:
        print("Authentication failed.")
    
# Check if the script is run directly, then call the main function
if __name__ == "__main__":
    main()
