from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from bot import DATABASE_URL, LOGGER


from pymongo import MongoClient
from bot import DATABASE_URL, LOGGER


def start():
    try:
        client = MongoClient("mongodb+srv://premiumbot:premiumbot@cluster0.5siafyp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db_name = "mydatabase"  # Specify your database name here
        db = client[db_name]  # Access the database
        return db
    except Exception as e:
        LOGGER.error(f'Error connecting to the database: {e}')
        exit(1)

db = start()





