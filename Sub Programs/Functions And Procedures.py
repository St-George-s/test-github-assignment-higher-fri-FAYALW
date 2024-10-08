# This is a function as it returns a value - in this case a variable called cup of type string
def drink_coffee(cup):
	cup = "empty"
	return cup
	
my_cup = "full"
after_drinking = drink_coffee(my_cup)
	
print(my_cup) # Output: "full"
print(after_drinking) # Output: "empty


# This is a procedure as it doesn't return any values
def add_glitter(bag): 
	bag.append("glitter")
	    
my_bag = ["keys", "wallet", "phone"]    
add_glitter(my_bag)
print(my_bag) # Output: ["keys", "wallet", "phone", "glitter"]