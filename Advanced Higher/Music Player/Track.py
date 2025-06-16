"""
Creating a blueprint for Track objects
- Title is a string
- Artist is a string
- Length is an integer
"""
class Track: #Creating a blueprint for track objetcs
    def __init__(self, title, artist,length): #This is the constructor. It is called when an object is created
        self.title = title
        self.artist = artist
        self.length = length

    def isLong(self):
        if self.length > 240:
            print("True")
        else:
            print("False")

    def showTrack(self): #This is a method to print the title and artist of an object
        print(f"Title: {self.title} - Artist: {self.artist}")
        print(f"Length: {self.length//60} minutes and {self.length%60} seconds")