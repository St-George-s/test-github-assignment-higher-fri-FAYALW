from Track import Track

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