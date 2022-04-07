from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DeclarativeBase = declarative_base()

class apples(DeclarativeBase):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    amount = Column('amount',Integer)

class faces(DeclarativeBase):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)

    role = Column('role',String)
    username = Column('username',String)
    password = Column('password',String)

def session():
    engine = create_engine('postgresql+psycopg2://rmjkkfztznehnk:de9e4eddba3aadccff525097dc8c85e3a7b25529a591b21f906cb0e6298f129b@ec2-54-157-79-121.compute-1.amazonaws.com:5432/d4tsi97rnohqqf')
    DeclarativeBase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

class init:
    def __init__(self):
        s = session()
        item = faces(role = 'seller', username = 'Manuel', password = 'Manuel')
        s.add(item)
        s.commit()

        item = faces(role = 'buyer', username = 'Frabian', password = 'Frabian')
        s.add(item)
        s.commit()

        item = apples(amount = 10)
        s.add(item)
        s.commit()

if __name__=='__main__':
    init()