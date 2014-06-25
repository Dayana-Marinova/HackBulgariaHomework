from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


Base = declarative_base()


class User(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

    def __str__(self):
        return "{} - {}".format(self.name, self.score)

    def __repr__(self):
        return self.__str__()

    def get_score(self):
        return self.score


engine = create_engine("sqlite:///university.db")
Base.metadata.create_all(engine)


def add_player():
    session = Session(bind=engine)
    name = input('Enter your name: ')
    player = User(name=name, score=0)
    session.add(player)
    session.commit()
    return player


print(add_player())


def highscores():
    pass
