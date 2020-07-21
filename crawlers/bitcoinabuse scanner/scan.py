from requests import get
import tqdm 
import time

TOKEN = ''
l = [i.splir()[0] for i in open('baddr','r').readlines()]
DATA = []

for i in tqdm.notebook.tqdm(set(l)):
    QUERY = "https://www.bitcoinabuse.com/api/reports/check?address={}&api_token={}"
    data = get(QUERY.format(i,TOKEN)).text
    time.sleep(1.2)
    print(data)
    DATA.append(data)