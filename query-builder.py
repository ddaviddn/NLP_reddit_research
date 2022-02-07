import configparser
import pandas as pd
import pymongo
from bson.regex import Regex
from pymongo import MongoClient
from datetime import datetime


# Read configuration file:
config = configparser.ConfigParser()

# Provide the path for the file with your information:
config.read(r"/home/david/School/spr-2021/ein-4912/mongo_reddit.conf")

# Make connection with MongoDB database:
# Uses the config file that you created
client = pymongo.MongoClient(host=config['MongoDB']['host'],
                              authSource=config['MongoDB']['db'],
                              port=int(config['MongoDB']['port']),
                              username=config['MongoDB']['user'],
                              password=config['MongoDB']['pass'],
                              authMechanism='SCRAM-SHA-256')

# Specify database and collection
database = client.reddit 

# Keep track of the time 
# start_time = time.time()

# Query - you can get this from studio 3T
print("Which database are you collecting from?\nex: comments_20xx-xx")
tablename = input()
collection = database[f"{tablename}"]

################################## Put Query HERE #############################

query = {}
print("What is the subreddit name you are collecting from?\nex: The_Donald")
subreddit = input()

query["subreddit"] = subreddit

projection = {}
projection["body"] = u"$body"
projection["subreddit"] = u"$subreddit"
projection["_id"] = 0

cursor = collection.find(query, projection = projection)

###############################################################################

mongo_docs = list(cursor)

print ("total docs:", len(mongo_docs))

data = pd.DataFrame.from_dict(mongo_docs)
print(data.head())

print("\nExporting file to csv.")
print("\nWhat is the name of your file? (filename only, no csv extension)")
filename = input()
data.to_csv(f"{filename}.csv", ",")

