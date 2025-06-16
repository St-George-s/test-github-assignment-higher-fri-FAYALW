from Track import Track
from albumTrack import AlbumTrack

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