#!/usr/bin/python3
""" 14. Cities in state """
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()
    cities = session.query(City).order_by(City.state_id.asc()).all()

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()
