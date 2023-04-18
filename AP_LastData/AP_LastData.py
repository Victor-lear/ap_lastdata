# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 10:47:40 2023

@author: victor
"""

import pymongo
from pymongo import MongoClient

def Search(DB, Collection,Search={}):
    global mongo_url_01,mongo_url_02
    try:
        conn = MongoClient(mongo_url_01) 
        db = conn[DB]
        collection = db[Collection]
        cursor=collection.find(Search)
        data=[d for d in cursor]
    except:
        data="Error"
    if data==[]:
        return False
    else:
        return data
def insert(Data):
	if False:
	   if data:
	#先把資料丟到Search確認有沒有這個資料有就更改沒有就新增
	#insert:collection.insert(new_data)
	#update:collection.update_one(selector, data) data = { "$set": { "Name":Name}}
def delete(Data):
	