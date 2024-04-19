#!/usr/bin/python3
"""
This script lists all State objects,
and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """engine to get states and 3 arguments"""

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(State).order_by(State.id).all()

    for state in results:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
