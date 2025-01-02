# Not doing this now whatever.

from pymongo import MongoClient
import os
value = os.environ.get("MONGO_URI")
print(value)
# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")

# # Access a database
# db = client["mydatabase"]

# # Access a collection
# collection = db["mycollection"]

# # Insert a document
# document = {"name": "Alice", "age": 25, "city": "New York"}
# result = collection.insert_one(document)
# print("Inserted document ID:", result.inserted_id)

# # Find all documents
# for doc in collection.find():
#     print(doc)

# # Close the connection
# client.close()