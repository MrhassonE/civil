from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.engine.url import URL


# Creating a database URL
postgres_db = {'drivername': 'sqlite',
               'database': 'db.sqlite'}
db_url = URL(**postgres_db)


# creating Base
Base = declarative_base()


# creating table of Arabic language
class CivilA(Base):
    __tablename__ = 'civilA'
    id=Column(Integer, primary_key=True)
    continent=Column('continent', String(32))
    country=Column('country', String(32))
    era=Column('era', String(32))
    remnant_name=Column('remnant_name', String(32))
    location=Column('location', String(32))
    description=Column('description', Text)
    gps_merdians=Column('gps_merdians', String(32))
    gps_latitudes=Column('gps_latitudes', String(32))

    
# creating table of English language
class CivilE(Base):
    __tablename__ = 'civilE'
    id=Column(Integer, primary_key=True)
    continent=Column('continent', String(32))
    country=Column('country', String(32))
    era=Column('era', String(32))
    remnant_name=Column('remnant_name', String(32))
    location=Column('location', String(32))
    description=Column('description', Text)
    gps_merdians=Column('gps_merdians', String(32))
    gps_latitudes=Column('gps_latitudes', String(32))


# creating the engine

engine = create_engine(db_url, echo=True)
Base.metadata.create_all(bind=engine)
