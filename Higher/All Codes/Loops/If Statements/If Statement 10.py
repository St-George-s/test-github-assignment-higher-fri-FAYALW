# Determines whether you are an adult or a child based on your age

# Prompt the user to enter their age and convert the input to an integer
age = int(input("enter age: "))  

# Check if the age is 18 or older
if age >= 18:  
    # If the age is 18 or older, print 'adult'
    print("adult")  
else:  
    # If the age is less than 18, print 'child'
    print("child")  
