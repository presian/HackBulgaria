import unittest
from playlist import Playlist
from song import Song


class SongListTest(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist(name="Code", repeat=True, shuffle=True)
        self.song = Song(title="Tra-la-la", artist="Pesho", album="Tarara", length="3:33")

    def test_getName(self):
        self.assertEqual("Code", self.playlist.getName())

    def test_getRepeat(self):
        self.assertTrue(self.playlist.getRepeat())

    def test_getShuffle(self):
        self.assertTrue(self.playlist.getShuffle())

    def test_getSongList(self):
        self.assertListEqual(self.playlist.getSongList(), [])

    def test_addSong(self):
        self.playlist.addSong(self.song)
        self.assertListEqual(self.playlist.getSongList(), [self.song])

    def test_removeSong(self):
        self.playlist.addSong(self.song)
        self.playlist.removeSong(self.song)
        self.assertListEqual(self.playlist.getSongList(), [])

    # this test not work
    # def test_addSongs(self):
    #     a = [self.song]
    #     b = Song(title="La-la", artist="Gosho", album="Tarara", length="5:33")
    #     a.append(b)
    #     self.playlist.addSongs(a)
    #     self.assertListEqual(self.playlist.getSongList(), a)


if __name__ == '__main__':
    unittest.main()
