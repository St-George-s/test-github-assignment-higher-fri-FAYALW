import csv

#Arrays:
studentID = []
firstName = []
lastName = []
grade = []

with open('File Handling/students.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skips the header
    for row in reader:
        print(row)

        studentID.append(row[0])
        firstName.append(row[0])
        lastName.append(row[0])
        grade.append(row[0])

        print("The student ID is",row[0],"the first name is",row[1], 
            "the last name is",row[2],"and the grade is",row[3])  # Prints each row