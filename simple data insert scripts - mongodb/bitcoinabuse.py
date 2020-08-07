import pymongo
from requests import get
import time
import pandas as pd
import json


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["SCAN"]
col = db["bitcoinabuse"]

TOKEN = ''
l = [i.split()[0] for i in open('baddr','r').readlines()]


for i in set(l):
    QUERY = "https://www.bitcoinabuse.com/api/reports/check?address={}&api_token={}"
    data = get(QUERY.format(i,TOKEN)).text
	data = json.loads(data)
	data['adddress']=i
	col.insert_one(data)
	time.sleep(6.0)

