# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, Friend Finder!")
# File is automatically closed after the indented block


# Writing to a CSV file
import csv

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])
# File is automatically closed after the indented block