from sqlalchemy.orm import Session
from connection import Base, engine
from movies import Movie
from projections import Projection
from reservation import Reservation

def main():

    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    all_movies = session.query(Movie).all()
    print(all_movies)
    all_projections = session.query(Projection).all()
    print(all_projections)

if __name__ == '__main__':
    main()












