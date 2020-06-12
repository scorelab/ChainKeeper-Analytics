#!/usr/bin/env python
# coding: utf-8


import json
import pandas as pd
from tqdm  import tqdm
from requests import get
from bs4 import BeautifulSoup
from collections import defaultdict as ddict
from datetime import datetime
from time import sleep



URL_home = 'http://www.walletexplorer.com/api/1/wallet-addresses?wallet=BitLaunder.com&from=0&count=100&caller=###'
URL_tx = 'http://www.walletexplorer.com/api/1/address?address={}&from=0&count=100&caller=####'


response = get(URL_home)


data = json.loads(response.text)



for i in tqdm(data.get('addresses')):
    tx_data = get(URL_tx.format(i.get('address')))
    i['tx data']=json.loads(tx_data.text)
    sleep(2)


FILENAME = datetime.now().strftime("%y-%m-%d")+' BitLaunder.com.json'


with open(FILENAME, 'w') as outfile:
    json.dump(data, outfile)