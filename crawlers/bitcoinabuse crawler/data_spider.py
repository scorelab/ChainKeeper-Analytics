import json
import requests
import re
from tqdm import tqdm
from hashlib import md5
import pandas as pd
from collections import defaultdict as dic
from datetime import datetime
import os

FILENAME = datetime.now().strftime("%m-%d-%Y")
credentials = json.load(open('./credentials.json','r'))

def getbitcoinabusedata():
    URL = 'https://www.bitcoinabuse.com/api/download/1d?api_token={}'.format(credentials.get('bitcoin'))
    request = requests.get(URL)
    if request.status_code == 200:
        open('bitcoinabuse {} .csv'.format(FILENAME),'wb').write(request.content)

def scanyoutubeurls(url):
    try:
        v_id = url.split('v=')[-1]
        URL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={}&key={}'.format(v_id,credentials.get('youtube'))
        request = requests.get(URL)
        if request.status_code == 200:
            open('{}.json'.format(v_id),'wb').write(request.content)
            return v_id
        else:
            return 'error '+str(request.status_code)
    except:
        pass

def main():
    getbitcoinabusedata()
    DF = dic(list)
    data = pd.read_csv('bitcoinabuse {} .csv'.format(FILENAME))
    for index, row in tqdm(data.iterrows()):
        description = row.description
        bitcoinaddr = row.address
        urls = re.findall(r'(https?://\S+)', description)
        if urls != []:
            for i in urls:
                if 'www.youtube.com' in i:
                    scan_report = scanyoutubeurls(i)
                    try:
                        DF['link file'].append(scan_report+".json")
                        DF['abuse addr'].append(bitcoinaddr)
                    except:
                        pass
    DF = pd.DataFrame(DF)
    DF.to_csv('map {} .csv'.format(FILENAME))

    
if __name__ == "__main__":
    main()