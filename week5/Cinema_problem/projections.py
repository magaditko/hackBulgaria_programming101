from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from connection import Base


class Projection(Base):
    __tablename__ = 'projections'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    date = Column(String)
    time = Column(String)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movies = relationship("Movie", backref="projections")

    def __str__(self):
        return '[{}] - {} {} ({})'.format(self.id, self.date, self.time, self.type)

    def __repr__(self):
        return self.__str__()
