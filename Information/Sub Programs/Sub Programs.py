#In the code below, the code to add a new user to the array is repeated. We can make this code more efficient by using a subprogram  

#Code without a subprogram
# Define a User class (record)
class User:
    def init__(self, username, age, hobbies):
        self.username = username
        self.age = age
        self.hobbies = hobbies

# List of users (array of records) 
users = []

# Create a new user and add to the list of users 
new_user = User("john_doe", 15, ["reading", "swimming", "coding"]) 
users.append(new_user)

# Create a new user and add to the list of users 
new_user = User("jane_doe", 12, ["painting", "dancing"]) 
users.append(new_user)

print(users[0].username, users[0].age, users[0].hobbies)

#Code with a subprogram
# Create a new user and add to the list of users 
def create_profile(username, age, hobbies):
    new_user = User(username, age, hobbies) 
    users.append(new_user)

# Example usage
create_profile("john_doe", 15, ["reading", "swimming", "coding"]) 
create_profile("jane_doe", 12, ["painting", "dancing"])