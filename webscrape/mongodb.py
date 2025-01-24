# Not doing this now whatever.
from dotenv import load_dotenv
from pymongo import MongoClient
import os
import json


def setup():
  load_dotenv() 
  value = os.environ.get("MONGO_URI")

  client = MongoClient(value)
  return client

def close(client):
  client.close()

def insert(document, db_name):
  client = setup()
  db = client["TangoBot"]
  collection = db[db_name]
  result = collection.insert_one(document)
  print("Inserted document ID:", result.inserted_id)
  close(client)

def get():
  client = setup()
  db = client['TangoBot']
  collection = db['Boards']
  boards = list(collection.find())
  close(client)
  return boards

def delete(date):
  client = setup()
  db = client["TangoBot"]
  collection = db["SolvedBoards"]
  query = {"date": date}
  result = collection.delete_many(query)
  print(f"Deleted {result.deleted_count} document(s)")
  close(client)


# if __name__=="__main__":
  # get()
  # insert({"a":1,"b":2,"c":3})
  

