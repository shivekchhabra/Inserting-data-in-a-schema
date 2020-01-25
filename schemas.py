import os
import pandas as pd
import sqlalchemy.sql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, DateTime, BigInteger, BIGINT

# Overview:
# This code is for creating a table with schema in a data base.
# Please use your database credentials in the db_string

Base = declarative_base()


# Class for creating a table with a schema
class MyTable(Base):
    __tablename__ = 'table_xyz'
    __table_args__ = {'extend_existing': True}

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    dob = Column(Date, nullable=True)


# Function to insert data in the table created
def table_xyz(filename, *datecols):
    # Please note the db credentials are stored as environement variables. Please use your own credentials.
    db_string = "postgres+psycopg2://{}:{}@{}/{}".format(os.environ['USER'], os.environ['PWD'],
                                                         os.environ['HOST'],
                                                         os.environ['DB'])

    engine = create_engine(db_string)
    Base.metadata.create_all(engine)
    print('schema_created')
    data = pd.read_csv(filename)
    if datecols != []:
        for i in datecols:
            data[i] = pd.to_datetime(data[i], dayfirst=True)
    data.fillna(sqlalchemy.sql.null(),
                inplace=True)  # This is for converting the NAN, NAT values for sqlalchemy to be able to handle them.
    Session = sessionmaker(engine)
    session = Session()
    ct = 0
    for idx, row in data.iterrows():
        new_entry = MyTable(name=row['Name'],
                            age=row['Age'],
                            dob=row['Date of Birth'])
        session.add(new_entry)
        session.commit()
        print("Written for Row {} of {}".format(ct, len(data)))
        ct += 1

    session.close()
    print('values added')


if __name__ == '__main__':
    file = 'test_data.csv'
    dates = 'Date of Birth'
    table_xyz(file, dates)
