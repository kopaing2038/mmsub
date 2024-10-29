
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from bot import DATABASE_URL, LOGGER


from pymongo import MongoClient
from bot import DATABASE_URL, LOGGER



def start():
    try:
        # Initialize the MongoDB client
        client = MongoClient("mongodb+srv://premiumbot:premiumbot@cluster0.5siafyp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        # Access the desired database
        db = client['dvdv']  # Replace with your actual database name
        return db
    except Exception as e:
        LOGGER.error(f'Failed to connect to the database: {e}')
        exit(1)

# Start the database connection
DATABASE = start()



BASE = declarative_base()
SESSION = start()




