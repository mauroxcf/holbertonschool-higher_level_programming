#!/usr/bin/python3
""" lists all State objects from the database """
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
