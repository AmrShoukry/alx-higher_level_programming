#!/usr/bin/python3
""" 10. Get a state """
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

import os
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
DB_URI = os.path.join(ROOT_PATH, 'my_database.db')
engine = create_engine(f"sqlite:///{DB_URI}", echo=True)
    
if __name__ == "__main__":
    # engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    #     sys.argv[1],
    #     sys.argv[2],
    #     sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
