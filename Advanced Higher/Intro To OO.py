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

    def is_long(self):
        if self.length > 240:
            print("True")
        else:
            print("False")

    def show_track(self): #This is a method to print the title and artist of an object
        print(f"Title: {self.title} - Artist: {self.artist}")
        print(f"Length: {self.length//60} minutes and {self.length%60} seconds")

"""
Creating a blueprint for AlbumTrack objects
- Inherits Track
- Album name is a string
"""
class AlbumTrack(Track):
    def __init__(self, title, artist, length, album_name):
        super().__init__(title, artist, length) #Creates an instance of Track object
        self.album_name = album_name

    def get_album(self):
        return self.album_name
    
    def show_track(self):
        super().show_track()
        print(f"Album Name: {self.album_name}")

"""
Main program
"""
song = Track("Sultans of Swing", "Dire Straits", 128) #Create an instance of the object Track (calls the constructor)
song.show_track()
song.is_long()

fav = Track("Focus", "Ariana Grande", 240)
fav.show_track()
fav.is_long()

mySongFromAlbum = AlbumTrack("I Love Coding", "Kevin Rodger", 400, "St G's For Life")
mySongFromAlbum.show_track()
print(mySongFromAlbum.get_album())

#print(fav.get_album()) - This will not work as get_album only exists on Track, not AlbumTrack