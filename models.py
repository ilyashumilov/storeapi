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
    engine = create_engine('postgresql+psycopg2://kgymkjkyzwwdzm:ba0a643ecd2daeff4c8074bc1feb3e4e1edb1fb20742d42265ad9a17349c31fb@ec2-3-217-251-77.compute-1.amazonaws.com:5432/d7gde9hja1e92a',connect_args={'sslmode':'require'}, echo=True)
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

#if __name__=='__main__':
#    init()
    