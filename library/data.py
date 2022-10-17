from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy import Column, SmallInteger, String, Integer

engine = create_engine('postgresql://aktai:1@localhost:5432/dater')

Base = declarative_base()


class Money(Base):
    __tablename__ = 'money'
    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    name = Column(String(30))
    nick = Column(String(30))
    cash = Column(Integer)
    telegram_id = Column(String(10))

    def __repr__(self):
        return f'{self.name} {self.nick} {self.cash}'


Session = sessionmaker(bind=engine)
session = Session()


def create_data(name, nick, cash, telegram_id):
    session.add(Money(telegram_id=telegram_id, name=name, nick=nick, cash=cash))
    session.commit()


def data():
    data = session.query(Money.telegram_id).all()
    list_ = []
    for z in data:
        for c in z:
            list_.append(c)
    return list_



def schet(tg_id):
    acha = session.query(Money.cash).filter(Money.telegram_id == str(tg_id)).all()
    a = [x for i in acha for x in i]
    print(a)
    return a[0]
# a = session.query(Money.id).all()
# print(a)

# session.commit()
# a = len(session.query(Money).all())
# print(a)
# while a != 0:
#     session.query(Money).filter(Money.id == a).delete()
#     session.commit()
#     a -= 1
#     print(session.query(Money).all())


# def init_db():
#     Base.metadata.create_all(engine)
# init_db()
