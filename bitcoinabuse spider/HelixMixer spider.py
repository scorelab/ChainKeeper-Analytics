#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import pandas as pd
from tqdm  import tqdm
from requests import get
from bs4 import BeautifulSoup
from collections import defaultdict as ddict
from datetime import datetime
from time import sleep


# In[ ]:


URL_home = 'http://www.walletexplorer.com/api/1/wallet-addresses?wallet=HelixMixer&from=0&count=100&caller=###'
URL_tx = 'http://www.walletexplorer.com/api/1/address?address={}&from=0&count=100&caller=####'


# In[ ]:


response = get(URL_home)


# In[ ]:


data = json.loads(response.text)


# In[ ]:


for i in tqdm(data.get('addresses')):
    tx_data = get(URL_tx.format(i.get('address')))
    i['tx data']=json.loads(tx_data.text)
    sleep(2)


# In[ ]:


FILENAME = datetime.now().strftime("%y-%m-%d")+' HelixMixer.json'


# In[ ]:


with open(FILENAME, 'w') as outfile:
    json.dump(data, outfile)


# In[ ]:




