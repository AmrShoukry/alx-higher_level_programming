#!/usr/bin/python3
""" 6. First state model """
import sys
from sqlalchemy import connection, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
    '.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()
    states = session.query(State).order_by(State.id.asc).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
