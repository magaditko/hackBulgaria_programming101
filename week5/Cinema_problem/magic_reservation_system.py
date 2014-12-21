from sqlalchemy.orm import Session
from connection import Base, engine
from movies import Movie
from projections import Projection
from reservation import Reservation
from commands import CommandParser


class MagicReservationSystem():
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session(bind=engine)
    
    def add_movie(self, name, rating):
        movie = Movie(name=name, rating=rating)
        self.session.add(movie)
        self.session.commit()

    def show_all_movies(self):
        all_movies = self.session.query(Movie).order_by(Movie.rating).all()
        return all_movies

    def add_movie_projection(self, movie_id, type, date, time):
        movie = self.session.query(Movie).filter(Movie.id==movie_id).one()
        movie.projections = [Projection(type=type, date=date, time=time)]
        self.session.commit()

    def show_projections(self, movie_id, date=''):
        if not date:
            projections = self.session.query(Projection).filter(Projection.movie_id==movie_id).order_by(Projection.date).all()
        else:
            projections = self.session.query(Projection).filter(Projection.movie_id==movie_id, Projection.date==date).all()
        return projections

    def show_projection(self, projection_id):
        projection = self.session.query(Projection).filter(Projection.id==projection_id).one()
        return projection

    def show_available_seats(self, projecton_id):
        taken_seats = self.session.query(Reservation).filter(Reservation.projection_id==projecton_id).count()
        return 100 - taken_seats

    def add_reservation(self, projection_id, username, row, col):
        is_available = self.check_availability(row, col)
        is_valid = self.check_validity(row, col)
        if is_available and is_valid:
            projection = self.show_projection(projection_id)
            projection.reservations.append(Reservation(username=username, row=row, col=col))
            self.session.commit()
        else:
            return "No"

    def tickets(self):
        num_tickets = int(input('number>'))
        username = input('name>')

            

    def check_validity(self, row, col):
        if row > 10 or col > 10:
            return False
        elif row < 0 or col < 0:
            return False
        else:
            return True

    def check_availability(self, row, col):
        seats = self.session.query(Reservation.row, Reservation.col).all()
        if (row, col) in seats:
            return False
        else:
            return True

    def start(self):
        cp = CommandParser()
        cp.add_command('show_movies', self.show_all_movies)
        cp.add_command('add_movie', self.add_movie)
        cp.add_command('add_projection', self.add_movie_projection)
        cp.add_command('show_projections', self.show_projections)
        cp.add_command('add_reservation', self.add_reservation)
        
        while True:
            user_input = input()
            if user_input == 'exit':
                break
            else:
                print(cp.execute(user_input))
            
mrs = MagicReservationSystem()
mrs.start()
