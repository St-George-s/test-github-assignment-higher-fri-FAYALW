def modify_list(lst):
    lst.append(4)
numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  # Output: [1, 2, 3, 4]

def modify_string(s):
    s = s + " World"
text = "Hello"
modify_string(text)
print(text)  # Output: "Hello"

#In the first case, the list numbers is modified because lists are mutable. In the second case, the string text remains unchanged outside the function because strings are immutable