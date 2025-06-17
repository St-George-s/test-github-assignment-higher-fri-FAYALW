from track import Track

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
    
    def show_track(self):
        super().showTrack()
        print(f"Album Name: {self.albumName}")