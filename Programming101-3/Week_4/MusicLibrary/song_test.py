import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song(title="Tra-la-la", artist="Pesho", album="Tarara", length="3:33")
        self.second_song = Song(title="Tra-la-la", artist="Pesho", album="Tarara", length="3:33")

    def test_getTitle_method(self):
        self.assertEqual("Tra-la-la", self.song.getTitle())

    def test_getArtist(self):
        self.assertEqual("Pesho", self.song.getArtist())

    def test_getAlbum(self):
        self.assertEqual("Tarara", self.song.getAlbum())

    def test_getLength(self):
        self.assertEqual("3:33", self.song.getLength())

    def test_str_(self):
        self.assertEqual("Pesho - Tra-la-la from Tarara - 3:33", str(self.song))

    def test_eq_(self):
        self.assertTrue(self.song == self.second_song)

    def test_hash_(self):
        self.assertTrue(type(hash(self.song)) == int)

    def test_length_without_arguments(self):
        self.assertEqual(self.song.length(), "3:33")

    def test_length_with_seconds(self):
        self.assertEqual(self.song.length(seconds=True), 213)

    def test_length_with_minutes(self):
        self.assertEqual(self.song.length(minutes=True), 3)

    def test_length_with_hours(self):
        self.assertEqual(self.song.length(hours=True), 0)

if __name__ == '__main__':
    unittest.main()
