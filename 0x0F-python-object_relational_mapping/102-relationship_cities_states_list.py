#!/usr/bin/python3
""" 17. From city """
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

    cities = session.query(City).order_by(City.id.asc()).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()