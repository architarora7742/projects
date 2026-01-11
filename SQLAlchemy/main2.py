from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

from main import Session

# ! It is going to map our Python classes to tables in the database so we are no longer going to create the tables
# ! But we are going to define classes and columns in these classes
# ! Individual rows as objects in Python and tables as classes in Python
# ! Relationship function __> I don't need to do a fancy join, I can access a list of objects. I can have a person a list of things objects that I can work with in Python without doing any fancy sql connections or joins


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

    person = relationship('Person', back_populates='things')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

new_person = Person(name="Charles", age=40)
session.add(new_person)
session.flush()

new_thing = Thing(description='Camera', value=500, owner=new_person.id)

session.add(new_thing)
session.commit()

print(new_person.things)
print(new_thing.person.name)


result = session.query(Person.name, Person.age).all() # It will return the tuple

print(result)
print([p.name for p in result])

print(session.query(Person).all())


result = session.query(Person).where(Person.age > 50).all()

result = session.query(Thing).filter(Thing.value < 100).delete()

session.commit()


result = session.query(Thing).filter(Thing.value < 100).all() # It will return the tuple

print(result)


result = session.query(Person).filter(Person.name == "Charlie").update({'name': 'charles'})

result = session.query(Person.name, Thing.description).join(Thing).all()

print(result)

result = session.query(Thing.owner, func.sum(Thing.value)).group_by(Thing.owner).having(func.sum(Thing.value) > 50).all()
print(result)


session.close() # It will close the connection and commit everything to the db 
