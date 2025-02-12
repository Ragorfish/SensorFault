from pymongo import MongoClient # type: ignore
import pandas as pd
import json

#url
uri="mongodb+srv://mohitsisodia200010:yRAHNnj47ZUeAeBo@cluster0.lii1w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME='waferfault'

df=pd.read_csv("C:\Users\imran\Dropbox\PC\Downloads\sensorproject\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)