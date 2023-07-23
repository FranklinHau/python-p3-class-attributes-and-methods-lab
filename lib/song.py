class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name= name
        self.artist= artist
        self.genre= genre
        self.__class__.add_song_to_count()
        self.__class__.add_to_genre(self.genre) 
        self.__class__.add_to_artist(self.artist)   
        self.__class__.add_to_genre_count(self.genre)
        self.__class__.add_to_artist_count(self.artist)    
        

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    @classmethod
    def add_to_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)   
    @classmethod
    def add_to_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

#song1 = Song("99 Problems", "Jay Z", "Rap")
#song2 = Song("Halo", "Beyonce", "Pop")
#song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
# Getting Total Count of Songs:
# print(Song.count) # This would print 3 as we have created three Song objects.
# #Getting Lists of All Genres and Artists:
# print(Song.genres) # prints ['Rap', 'Pop', 'Rock']
# print(Song.artists) # prints ['Jay Z', 'Beyonce', 'Nirvana']
# Counting Songs by Genre:
# print(Song.genre_count) # prints {'Rap': 1, 'Pop': 1, 'Rock': 1}
# #Counting Songs by Artist:
# print(Song.artist_count) # prints {'Jay Z': 1, 'Beyonce': 1, 'Nirvana': 1}

# # This code defines a class named Song which is intended to manage data about songs.

# # Class Variables:

# count: This class variable is used to keep track of the total number of songs (i.e., Song objects) created.
# genres: This list keeps track of the unique genres of all the songs.
# artists: This list keeps track of the unique artists of all the songs.
# genre_count: This dictionary keeps count of the number of songs for each genre. The keys are the genres, and the values are the counts.
# artist_count: This dictionary keeps count of the number of songs by each artist. The keys are the artists, and the values are the counts.
# Constructor (__init__):

# When a Song object is created, the constructor is called with name, artist, and genre parameters. The name, artist, and genre of the song are stored in instance variables.
# It also calls several class methods to update the class variables defined above.
# Class Methods:

# add_song_to_count: This method increments the count class variable by one each time a song is created.
# add_to_genre: This method adds the genre of the new song to the genres list only if it's not already in the list.
# add_to_artist: This method adds the artist of the new song to the artists list only if they're not already in the list.
# add_to_genre_count: This method updates the genre_count dictionary. It increments the count of the genre by one if the genre is already in the dictionary; otherwise, it adds a new entry with the genre as the key and 1 as the count.
# add_to_artist_count: This method works similarly to add_to_genre_count, but it updates the artist_count dictionary. It increments the count of the artist by one if the artist is already in the dictionary; otherwise, it adds a new entry with the artist as the key and 1 as the count.
# So, every time a Song object is instantiated, the code updates the overall song count, the list of genres, the list of artists, the count of songs per genre, and the count of songs per artist.
