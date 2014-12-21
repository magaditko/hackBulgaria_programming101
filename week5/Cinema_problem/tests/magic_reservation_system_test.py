import os
import sys
sys.path.insert(0, '..')
import unittest

from movies import Movie
from projections import Projection
from reservation import Reservation

from magic_reservation_system import MagicReservationSystem


class MRSTest(unittest.TestCase):
    def setUp(self):
        self.mrs = MagicReservationSystem()
        self.movie = Movie(name='test_movie', rating=3.5)
        self.projection = Projection(movie_id=1, type='3D', date='2014-04-01', time='19:10')
        self.projection2 = Projection(movie_id=1, type='2D', date='2014-04-02', time='23:10')
        self.reservation = Reservation(id=1, projection_id=1, username='shosh', row=1, col=1)
        
    def tearDown(self):
        os.remove('cinema.db')

    def test_add_movie(self):
        self.mrs.add_movie('movie', 1)
        result = self.mrs.session.query(Movie.id,
                                        Movie.name,
                                        Movie.rating).all()
        self.assertIn((1, 'movie', 1.0), result)

    def test_show_movies(self):
        self.mrs.session.add(self.movie)
        self.mrs.session.commit()
        result = self.mrs.show_all_movies()
        self.assertEqual([self.movie], result)

    # def test_show_movie_name_with_id(self):
    #     self.mrs.session.add(self.movie)
    #     self.mrs.session.commit()
    #     result = self.mrs.show_movie_name(1)
    #     self.assertEqual('test_movie', result)

    def test_add_movie_projection(self):
        self.mrs.session.add(self.movie)
        self.mrs.add_movie_projection(1, '3D', '2014-04-10', '19:10')
        result = self.mrs.session.query(Projection.id, Projection.type, Projection.date, Projection.time).all()
        self.assertIn((1, '3D', '2014-04-10', '19:10'), result)

    def test_show_projections_without_date(self):
        self.mrs.session.add(self.projection)
        self.mrs.session.commit()
        result = self.mrs.show_projections(1)
        self.assertEqual([self.projection], result)

    def test_show_projections_with_date(self):
        self.mrs.session.add(self.projection)
        self.mrs.session.add(self.projection2)
        self.mrs.session.commit()
        result = self.mrs.show_projections(1, '2014-04-02')
        self.assertEqual([self.projection2], result)

    def test_show_available_seats(self):
        self.mrs.session.add(self.projection)
        self.mrs.session.commit()
        result = self.mrs.show_available_seats(1)
        self.assertEqual(100, result)

    def test_show_projection(self):
        self.mrs.session.add(self.projection)
        self.mrs.session.add(self.projection2)
        result = self.mrs.show_projection(1)
        self.assertEqual(self.projection, result)

    def test_add_reservation(self):
        self.mrs.session.add(self.projection)
        self.mrs.session.commit()
        self.mrs.add_reservation(1, 'shosh', 2, 2)
        result = self.mrs.session.query(Reservation.id, Reservation.projection_id, Reservation.username, Reservation.row, Reservation.col).all()
        # projection_id and reservation_id
        self.assertIn((1, 1, 'shosh', 2, 2), result)

        self.assertEqual(self.mrs.show_available_seats(1), 99)

    def test_check_availability(self):
        self.mrs.session.add(self.reservation)
        self.assertTrue(self.mrs.check_availability(1, 2))
        self.assertFalse(self.mrs.check_availability(1, 1))

    def test_check_validity(self):
        self.assertTrue(self.mrs.check_validity(3, 5))
        self.assertFalse(self.mrs.check_validity(-2, 1))
        self.assertFalse(self.mrs.check_validity(11, 5))
        
    def test_start(self):
        self.mrs.start()
        
if __name__ == '__main__':
    unittest.main()
