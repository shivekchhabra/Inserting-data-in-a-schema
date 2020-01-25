## What does this repository contain?
This repository contains a code to insert data in a postgreSQL database using sqlalchemy-orm and psycopg2-binary.

Suppose you have a csv file of the data and you want to push it to a database, df.to_sql is one option but it hurts in many ways in the longer run. For instance, it conflicts with object type variables and percentage symbols.

Hence, it is always advisable to set a schema for every table.


## How to use this repository.
Start by installing requirements 
	pip install -r requirements.txt

After that checkout schemas.py

You may add more tables and functions to it. Please remember to use your own credentials. For the demo purpose, I have used a local database and passed my credentials in environment variables.
You may customise the code according to your need.
