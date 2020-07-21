from requests import get
import tqdm 
import time
import pandas as pd
import json

TOKEN = ''
l = [i.split()[0] for i in open('baddr','r').readlines()]
DATA = []

for i in tqdm.notebook.tqdm(set(l)):
    QUERY = "https://www.bitcoinabuse.com/api/reports/check?address={}&api_token={}"
    data = get(QUERY.format(i,TOKEN)).text
    time.sleep(1.2)
    print(data)
    DATA.append(data)

DATA = list(map(json.loads,DATA))
DATA = pd.DataFrame(DATA)
DATA.to_csv("scan_repote.csv")