#classes

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics


    def sing_my_song(self):
        for line in self.lyrics :
            print(line)

    def sing_my_song_reversed(self):
        for line in reversed(self.lyrics):
            print(line)


happy_bday =[
        'Happy birthday to you',
        'I dont want to get sued',
        'So I will stop right there'
]

bulls_on_parade = [
        'They rally around tha family',
        'With pockets full of shells'
]

# initiate class 
song_1 = Song(happy_bday)
song_2 = Song(bulls_on_parade)

song_1.sing_my_song()
song_1.sing_my_song_reversed()

# song_2.sing_my_song()
