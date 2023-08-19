#!/usr/bin/python3
""" 6. First state model """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ states Table """
    __tablename__ = "states"
    id = Column(Integer(), primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
