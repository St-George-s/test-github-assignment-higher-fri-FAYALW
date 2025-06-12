from Track import Track
from albumTrack import AlbumTrack

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