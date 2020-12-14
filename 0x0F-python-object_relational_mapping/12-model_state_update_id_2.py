#!/usr/bin/python3
"""  changes the name of a State object from the database """
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    session.query(State).filter(State.id == 2).update({'name': 'New Mexico'})
    session.commit()

    session.close()
