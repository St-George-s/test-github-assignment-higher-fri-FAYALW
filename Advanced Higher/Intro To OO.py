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

"""
Creating a blueprint for AlbumTrack objects
- Inherits Track
- Album name is a string
"""
class AlbumTrack(Track):
    def __init__(self, title, artist, length, albumName):
        super().__init__(title, artist, length) #Creates an instance of Track object
        self.albumName = albumName

    def getAlbum(self):
        return self.albumName
    
    def showTrack(self):
        super().showTrack()
        print(f"Album Name: {self.albumName}")

"""
Main program
"""
song = Track("Sultans of Swing", "Dire Straits", 128) #Create an instance of the object Track (calls the constructor)
song.showTrack()
song.isLong()

fav = Track("Focus", "Ariana Grande", 240)
fav.showTrack()
fav.isLong()

mySongFromAlbum = AlbumTrack("I Love Coding", "Kevin Rodger", 400, "St G's For Life")
mySongFromAlbum.showTrack()
print(mySongFromAlbum.getAlbum())

#print(fav.getAlbum()) - This will not work as get_album only exists on Track, not AlbumTrack