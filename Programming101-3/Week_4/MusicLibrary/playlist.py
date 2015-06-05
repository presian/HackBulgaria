from song import Song


class Playlist:

    def __init__(self, name="", repeat=False, shuffle=False):
        self.__name = name
        self.__repeat = repeat
        self.__shuffle = shuffle
        self.__list = []

    def getName(self):
        return self.__name

    def getRepeat(self):
        return self.__repeat

    def getShuffle(self):
        return self.__shuffle

    def getSongList(self):
        return self.__list

    def addSong(self, song):
        self.__list.append(song)

    def removeSong(self, song):
        # add checking for song existing
        self.__list.pop(self.__list.index(song))

    def addSongs(self, songs):
        return self.__list + songs
