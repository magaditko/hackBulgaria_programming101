import unittest

import sys
sys.path.insert(0, '../')

from playlist import Playlist
from song import Song


class PlaylistTest(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist('DnB')
        self.come_alive = Song(
            'Come Alive',
            'Netsky',
            'Netsky-2',
            2,
            204,
            320
        )
        self.puppy = Song(
            'Puppy',
            'Netsky',
            'Netsky-2',
            4,
            280,
            96
        )
        self.horrorcane = Song(
            'Horrorcane',
            'High Rankin',
            'Unknown',
            5,
            300,
            192
        )

        self.playlist.songs = [self.come_alive, self.puppy]

    def test_init(self):
        self.assertEqual(self.playlist.name, 'DnB')
        self.playlist.songs = []
        self.assertEqual(self.playlist.songs, [])

    def test_add_song(self):
        self.playlist.songs = []
        self.playlist.add_song(self.come_alive)
        self.assertEqual(self.playlist.songs, [self.come_alive])

    def test_remove_song(self):
        self.playlist.remove_song('Come Alive')
        self.assertEqual(self.playlist.songs, [self.puppy])

    def test_total_length(self):
        self.assertEqual(self.playlist.total_length(), 484)

    def test_remove_disrated(self):
        self.playlist.remove_disrated(3)
        self.assertEqual(self.playlist.songs, [self.puppy])

    def test_remove_bad_quality(self):
        self.playlist.remove_bad_quality()
        self.assertEqual(self.playlist.songs, [self.come_alive])

    def test_show_artists(self):
        self.playlist.songs.append(self.horrorcane)
        self.assertEqual(self.playlist.show_artists(), ['Netsky', 'High Rankin'])
        print(self.horrorcane)
        print(self.playlist)




if __name__ == '__main__':
    unittest.main()
