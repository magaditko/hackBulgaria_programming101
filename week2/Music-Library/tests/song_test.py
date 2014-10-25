import unittest

import sys
sys.path.insert(0, '../')

from song import Song


class SongTest(unittest.TestCase):
    def setUp(self):
        self.song = Song(
            'Come Alive',
            'Netsky',
            'Netsky-2',
            0,
            204,
            320
        )

    def test_init(self):
        self.assertEqual(self.song.title, 'Come Alive')
        self.assertEqual(self.song.artist, 'Netsky')
        self.assertEqual(self.song.album, 'Netsky-2')
        self.assertEqual(self.song.rating, 0)
        self.assertEqual(self.song.length, 204)
        self.assertEqual(self.song.bitrate, 320)

    def test_rate(self):
        self.song.rate(4)
        self.assertEqual(self.song.rating, 4)

    def test_rate_with_invalid_data(self):
        with self.assertRaises(ValueError):
            self.song.rate(50)

if __name__ == '__main__':
    unittest.main()
