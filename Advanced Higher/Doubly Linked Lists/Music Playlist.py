#A node stores data, and links to the next and previous nodes

class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None #First song in the playlist
        self.tail = None #Last song in the playlist

    def add_song(self, title):
        new_song = SongNode(title)
        if self.head is None:
            self.head = new_song
            self.tail = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song

    def play_forward(self):
        current = self.head
        while current:
            print("Now playing:", current.title)
            current = current.next

#Implement myself
    def play_backward(self):
        pass

#Searching forward through the playlist
    def find_song_forward(self, title):
        current = self.head
        while current:
            if current.title == title:
                return True
            current = current.next
        return False