#!/usr/bin/python3
"""  adds the State object “Louisiana” to the database """
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    add_state = State(name='Louisiana')
    session.add(add_state)
    session.commit()
    print(add_state.id)

    session.close()
