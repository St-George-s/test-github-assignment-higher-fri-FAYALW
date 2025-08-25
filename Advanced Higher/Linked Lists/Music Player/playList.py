class Playlist:
    def __init__(self, tracks, maxLength, playTime):
        self.tracks = tracks
        self.maxLength = maxLength
        self.playTime = playTime

    def addTrack(self, newTrack):
        if len(self.tracks) == self.maxLength:
            print("Error, too many tracks")
        else:
            self.tracks.append(newTrack)
            self.playTime = self.playTime + newTrack.length

    def findTitle(self, trackTitle):
        result = -1
        for index in range(0,self.maxLength-1):
            if self.tracks[index].title == trackTitle:
                result = index
        return result

    def deleteTrack(self, index):
        if index >= self.maxLength or index < 0:
            print("Error, invalid index")
        else:
            self.playTime == self.playTime - self.tracks[index].length
            del self.tracks[index]

    def showTracks(self):
        for counter in range(0,len(self.tracks)):
            self.tracks[counter].showTrack()