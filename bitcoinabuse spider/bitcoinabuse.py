#!/usr/bin/env python
# coding: utf-8

import json
import pandas as pd
from tqdm  import tqdm
from requests import get
from bs4 import BeautifulSoup
from collections import defaultdict as ddict
from datetime import datetime

class BreakOutOfALoop(Exception): pass

def main():
    FILENAME = datetime.now().strftime("%y-%m-%d")+'{}'
    URL = 'https://www.bitcoinabuse.com/reports?page={}'
    s ='div:nth-child(1) main:nth-child(3) div.container div.row:nth-child(3) > div.col-xl-4.col-md-6.mb-3:nth-child({})'
    data = ddict(list)
    page = 1
    while True:
        response = get(URL.format(page))
        soup = BeautifulSoup(response.text, 'html.parser')
        count = 1
        try:
            while True:
                try:
                    temp = soup.select(s.format(count))[0]
                    a = temp.find('a').text
                    i = temp.find('i').text
                    if i == '1 day ago' : raise BreakOutOfALoop
                    data['address'].append(a)
                    data['time'].append(i)
                    count+=1
                except IndexError:
                    break
            page+=1
        except BreakOutOfALoop:
            break
    data = pd.DataFrame(data)
    data.to_csv(FILENAME.format(' bitcoin abuse list.csv'))

    record_file = open(FILENAME.format(' bitcoin abuse reports.txt'),'w')
    rslt = []
    for index, row in tqdm(data.iterrows()):
        url = 'https://api.blockcypher.com/v1/btc/main/addrs/{}/balance'.format(row.address)
        data = get(url).text
        data = json.loads(data)
        url_ab_table = 'https://www.bitcoinabuse.com/reports/{}'.format(row.address)
        ab_table = get(url_ab_table)
        soup = BeautifulSoup(ab_table.text, 'html.parser')
        row_table = 1
        abuse_reports = []
        while True:
            try:
                parm1 = 'div.container.mb-4 table.table.table-striped.table-bordered.table-responsive-lg:nth-child(3) tbody:nth-child(2) tr:nth-child({}) > td:nth-child(1)'
                parm2 = 'div.container.mb-4 table.table.table-striped.table-bordered.table-responsive-lg:nth-child(3) tbody:nth-child(2) tr:nth-child({}) > td:nth-child(2)'
                parm3 = 'div.container.mb-4 table.table.table-striped.table-bordered.table-responsive-lg:nth-child(3) tbody:nth-child(2) tr:nth-child({}) > td:nth-child(3)'
                parm4 = 'div.container.mb-4 table.table.table-striped.table-bordered.table-responsive-lg:nth-child(3) tbody:nth-child(2) tr:nth-child({}) > td:nth-child(4)'
                temp = {'Abuse Date':soup.select(parm1.format(row_table))[0].text,
                        'Abuse Type':soup.select(parm2.format(row_table))[0].text,
                        'Abuser':soup.select(parm3.format(row_table))[0].text,
                        'Description':soup.select(parm4.format(row_table))[0].text
                       }
                abuse_reports.append(temp)
                row_table+=1
            except IndexError:
                break
        data['abuse_reports'] =  abuse_reports
        rslt.append(data)
    record_file.write('\n'.join(list(map(str,rslt))))
    record_file.flush()
    record_file.close()
    return 0


if __name__ == '__main__':
    main()