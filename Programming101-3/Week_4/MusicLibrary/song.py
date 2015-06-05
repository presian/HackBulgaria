class Song():

    def __init__(self, title="", artist="", album="", length=""):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__length = length

    def getTitle(self):
        return self.__title

    def getArtist(self):
        return self.__artist

    def getAlbum(self):
        return self.__album

    def getLength(self):
        return self.__length

    def length(self, seconds=False, minutes=False, hours=False):
        if seconds is False and minutes is False and hours is False:
            return self.getLength()
        lengt_as_parts = [x for x in self.__length.split(":")][::-1]
        lengt_as_seconds = sum([int(lengt_as_parts[i]) * 60 ** i for i in range(0, len(lengt_as_parts))])
        if seconds is True:
            return lengt_as_seconds
        if minutes is True:
            return lengt_as_seconds // 60
        if hours is True:
            return lengt_as_seconds // 360

    def __str__(self):
        return "{} - {} from {} - {}"\
            .format(self.__artist, self.__title,
                    self.__album, self.__length)

    def __eq__(self, other):
        return self.__title == other.__title\
            and self.__artist == other.__artist\
            and self.__album == other.__album\
            and self.__length == other.__length

    def __hash__(self):
        return hash(self.__title + self.__artist
                    + self.__album + self.__length)
