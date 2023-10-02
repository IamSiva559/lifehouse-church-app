from pymongo import MongoClient
import config

# Initialize MongoDB client and database
client = MongoClient(config.MONGO_URI)
db = client[config.MONGO_DB_NAME]
users_collection = db[config.USER_COLLECTION]


# Close the database connection
def close_database_connection():
    if client:
        client.close()
