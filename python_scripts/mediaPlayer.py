''' Media player queue '''

'''
        Most music player software allows users the chance to add songs to a playlist. Upon hitting
        the play button, all the songs in the main playlist are played one after the other. The
        sequential playing of the songs can be implemented with queues because the first song to be
        queued is the first song that is played. This aligns with the FIFO acronym. We shall
        implement our own playlist queue that plays songs in the FIFO manner.
'''

'''
        Basically, our media player queue will only allow for the addition of tracks and a way to
        play all the tracks in the queue. In a full-blown music player, threads would be used to
        improve how the queue is interacted with, while the music player continues to be used to
        select the next song to be played, paused, or even stopped
'''

from random import randint
import time

class Node():
    
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def enqueue(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        
    def dequeue(self):
        current = self.head
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            

class Track():
    
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 10)
# To create a few tracks and print out their lengths, we do the following:



class MediaPlayerQueue(Queue):
    
    def __init(self):
        super(MediaPlayerQueue, self).__init__()
        
    # add a track 
    def add_track(self, track):
        self.enqueue(track)
        
    def play(self):
        while self.count > 0:
            current_track_node = self.dequeue()
            print(f'Now Play {current_track_node.data.title}')
            time.sleep(current_track_node.data.length)
            

track1 = Track("white whistle")
track2 = Track("butter butter")
track3 = Track("Oh black star")
track4 = Track("Watch that chicken")
track5 = Track("Don't go")

print(track1.length)
print(track2.length)

media_player = MediaPlayerQueue()
media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)
media_player.play()