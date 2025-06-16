class PlayList:
    def __init__(self, tracks, next, maxLength, playTime):
        self.tracks = tracks
        self.next = next
        self.maxLength = maxLength
        self.playTime = playTime

def addTrack(self, newTrack):
    if self.next == self.maxLength:
        print("Error, too many tracks")
    else:
        self.tracks[self.next] = newTrack
        self.next += 1
        self.playTime = self.playTime + self.newTrack.length

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
        for counter in range(index,next-1):
            self.tracks[counter] == self.tracks[counter + 1]
        self.next == self.next - 1

def showTracks(self):
    for counter in range(0,next-1):
        self.tracks[counter].showTrack()