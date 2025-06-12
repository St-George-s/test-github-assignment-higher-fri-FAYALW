# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed after the indented block

#Using readline Method
#	• Read a Single Line:
with open('./example.txt', 'r') as file:
    first_line = file.readline()
    print(first_line)
	
#	• Read Multiple Lines Using a Loop:
with open('./example.txt', 'r') as file:
      line = file.readline()
      while line:
          print(line, end='')  # 'end' prevents adding extra newline
          line = file.readline()
	
#Using readlines Method
#	• Read All Lines into a List:
with open('../example.txt', 'r') as file:
    all_lines = file.readlines()
    for line in all_lines:
        print(line, end='')  # 'end' prevents adding extra newline


# Reading from a CSV file
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# File is automatically closed after the indented block