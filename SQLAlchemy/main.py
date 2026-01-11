from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# declarative base is now going to be the replacement for the meta-data class.

engine = create_engine("sqlite:///mydatabase.db", echo=True)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)


    things = relationship('Thing', back_populates='person')

class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Float)
    owner = Column(Integer, ForeignKey('people.id'))

    person = relationship("Person", back_populates="things")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# new_person = Person(name="Charlie", age=70)
# session.add(new_person)
# session.flush()
#
#
# new_thing = Thing(description="Camera", value=500, owner=new_person.id)
# session.add(new_thing)
#
# session.commit()
# print(new_person.things)
# print(new_thing.person)
#
#
#
# print([t.description for t in new_person.things])

result = session.query(Person.name, Person.age).filter(Person.age > 40).all()
print([p.name for p in result])

