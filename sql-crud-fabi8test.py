from sqlalchemy import (
    create_engine, Column, Integer, String, Float
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class based model for the "My_Vinyls" table
class My_Vinyls_Collection(base):
    __tablename__ = "My_Vinyls_Collection"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    artist = Column(String)
    label = Column(String)
    genre = Column(String)
    year = Column(Integer)
    bpm = Column(Float)


# instead of connecting to the databse directly, we will ask for a session
# create a new instance of sessionemaker, then point to our engine (the db)
Session = sessionmaker(db)
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our "Programmer" table
serve_it_up = My_Vinyls_Collection(
    title="Serve it up",
    artist="Sterling Void",
    label="Clone",
    genre="Italo",
    year="1989",
    bpm="118"
)

heligoland = My_Vinyls_Collection(
    title="Heligoland",
    artist="Massive Attack",
    label="The Vinyl Factory",
    genre="Trip Hop",
    year="2010",
    bpm="118"
)

hello_nasty = My_Vinyls_Collection(
    title="Hello Nasty",
    artist="Beastie Boys",
    label="Capitol Records",
    genre="Hip Hop",
    year="1998",
    bpm="100"
)

protection = My_Vinyls_Collection(
    title="Protection",
    artist="Massive Attack",
    label="Wild Bunch Records",
    genre="Trip Hop",
    year="1994",
    bpm="90"
)


# add each instances of our programmers to our session
# session.add(serve_it_up)
# session.add(heligoland)
# session.add(hello_nasty)
# session.add(protection)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(fabi8bit)

# commit our session to the database
session.commit()

# query the database to find all Programmers
myvinyls = session.query(My_Vinyls_Collection)
for myvinyl in myvinyls:
    print(
        myvinyl.id,
        myvinyl.artist,
        myvinyl.label,
        myvinyl.genre,
        myvinyl.year,
        myvinyl.bpm,
        sep="  |  "
    )