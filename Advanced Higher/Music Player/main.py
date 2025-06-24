from track import Track
from albumTrack import AlbumTrack
from playList import Playlist

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

playlist = Playlist([song,fav], 10, 0.0)
print(playlist.tracks[0].isLong())
playlist.addTrack(Track("Defying Gravity", "Idina Menzel", 420))
playlist.showTracks()