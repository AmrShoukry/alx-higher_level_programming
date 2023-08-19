#!/usr/bin/python3
""" 16. List relationship """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    states = session.query(State).order_by(State.id.asc()).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        sorted_cities = sorted(state.cities, key=lambda city: city.id)
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
