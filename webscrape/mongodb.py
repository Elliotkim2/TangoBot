# Not doing this now whatever.
from dotenv import load_dotenv
from pymongo import MongoClient
import os
import json


# # Insert a document
# document = {"name": "Alice", "age": 25, "city": "New York"}
# result = collection.insert_one(document)
# print("Inserted document ID:", result.inserted_id)

# # Find all documents
# for doc in collection.find():
#     print(doc)

def setup():
  load_dotenv() 
  value = os.environ.get("MONGO_URI")
  print(value[-30:])

  client = MongoClient(value) # Connect to MongoDB
  return client

def close(client):
  client.close()

def insert(document):
  client = setup()
  db = client["TangoBot"] # Access a database
  collection = db["Boards"] # Access a collection
  result = collection.insert_one(document)
  print("Inserted document ID:", result.inserted_id)
  close()

if __name__=="__main__":
  load_dotenv() 
  value = os.environ.get("MONGO_URI")
  print(value[-30:])
  # insert({"a":1,"b":2,"c":3})
  

