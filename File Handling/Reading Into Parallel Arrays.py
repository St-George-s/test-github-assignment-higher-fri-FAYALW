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
        

# Declare parallel arrays to store data from the CSV file.
entryID = []
location = []
forename = []
surname = []
jumps = []

# Define a function to read data from a CSV file and store it in parallel arrays.
def getQualifyingData():
  with open("athletes.csv", "r") as file:  # Open the file to read.
    reader = csv.reader(file)  # Use the csv module to read the file.

    # header = next(reader) Some files may have a header, if they don't, you can delete this line

    for row in reader:  # Loop through each row in the CSV file.
      # Append data to each parallel array. 
      entryID.append(row[0])
      location.append(row[1])
      forename.append(row[2])
      surname.append(row[3])
      jumps.append(int(row[4])) # Convert jump values from strings to integers.

  # Return the populated arrays to the caller.
  return entryID, location, forename, surname, jumps