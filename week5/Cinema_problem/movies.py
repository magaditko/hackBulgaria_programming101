from sqlalchemy import Column, String, Float, Integer
from connection import Base


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rating = Column(Float)

    def __str__(self):
        return '[{}] - {} ({})'.format(self.id, self.name, self.rating)

    def __repr__(self):
        return self.__str__()
