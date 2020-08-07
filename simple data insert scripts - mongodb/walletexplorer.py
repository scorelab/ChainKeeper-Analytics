import pymongo
from requests import get
import time
import pandas as pd
import json


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["SCAN"]
col = db["walletexplorer"]

l = [i.split()[0] for i in open('baddr','r').readlines()]
TOKEN = ''


for i in set(l):
    QUERY = "http://www.walletexplorer.com/api/1/address-lookup?address={}&caller={}"
    data = get(QUERY.format(i,TOKEN)).text
    data = json.loads(data)
    data['adddress']=i
    col.insert_one(data)
    print(data)
    time.sleep(6.0)
