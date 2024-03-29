#!/usr/bin/python3
""" 14. Cities in state """
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ states Table """
    __tablename__ = "cities"
    id = Column(Integer(), primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
    state = relationship('State', backref="myStates", uselist=False)
