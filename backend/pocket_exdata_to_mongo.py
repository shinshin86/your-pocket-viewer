# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import pymongo


def db_connect():
    client = pymongo.MongoClient('localhost', 27017)
    return client.your_pocket_viewer


def main():
    db = db_connect()
    col = db['items']

    with open('ril_export.html', 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'lxml')
    plist = soup.find_all("li")
    d = {}
    for i in plist:
        d = {"url": i.a["href"],
             "tags": i.a["tags"],
             "time_added": i.a["time_added"],
             "id": i.a["time_added"],
             "title": i.string}
        col.update_one({'id': d['id']}, {'$set': d}, upsert=True)


main()
