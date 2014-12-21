from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from connection import Base


class Reservation(Base):
    __tablename__ = 'reservationn'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    row = Column(Integer)
    col = Column(Integer)
    projection_id = Column(Integer, ForeignKey("projection.id"))
    projection = relationship("Porjection", backref="reservations")

    def __str__(self):
        '[{}] - {} {} ({}, {})'.format(self.id,
                                       self.username,
                                       self.projection_id,
                                       self.row,
                                       self.col)

    def __repr__(self):
        return self.__str__()
