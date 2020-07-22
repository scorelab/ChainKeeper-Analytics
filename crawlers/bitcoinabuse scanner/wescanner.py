from requests import get
import tqdm 
import time
import pandas as pd
import json

l = [i.split()[0] for i in open('baddr','r').readlines()]
TOKEN = ''
DATA = []

for i in tqdm.notebook.tqdm(set(l)):
    QUERY = "http://www.walletexplorer.com/api/1/address-lookup?address={}&caller={}"
    data = get(QUERY.format(i,TOKEN)).text
    time.sleep(3.3)
    print(data)
    DATA.append(data)
    
DATA = list(map(json.loads,DATA))
DATA = pd.DataFrame(DATA)
DATA.to_csv("scan_reporte_we.csv")