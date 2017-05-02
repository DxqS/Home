# coding:utf-8
'''
Created on 2017/4/26.

@author: chk01
'''
from pymongo import MongoClient

mdb = MongoClient("localhost", 27017)
mdb = mdb["dxq"]

mdb.tt.insert({"_id":1,"name":"Dxq"})
