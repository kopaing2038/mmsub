
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from bot import DATABASE_URL, LOGGER


from pymongo import MongoClient
from bot import DATABASE_URL, LOGGER

def start():
    try:
        client = MongoClient("mongodb+srv://premiumbot:premiumbot@cluster0.5siafyp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client.get_default_database()  # Gets the default database
        return db
    except Exception as e:
        LOGGER.error(f'Error connecting to the database: {e}')
        exit(1)

DATABASE = start()



BASE = declarative_base()
SESSION = start()




