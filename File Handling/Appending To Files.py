# Appending to a file
with open('example.txt', 'a') as file:
    file.write("\\\\nAppending this line.")
# File is automatically closed after the indented block


# Appending to a CSV file
import csv

with open('data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Bob", 30])
# File is automatically closed after the indented block