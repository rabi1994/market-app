import pymongo

try:
    client = pymongo.MongoClient("mongodb://192.168.1.82:27017/",serverSelectionTimeoutMS=5000)
    # Attempt to retrieve server information
    server_info = client.server_info()
    print("Connected to MongoDB server:", server_info)
except pymongo.errors.ServerSelectionTimeoutError as err:
    print("Connection failed:", err)