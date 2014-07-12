#!/usr/bin/env python
from pymongo import Connection
import time,datetime
import os,sys

connection = Connection('127.0.0.1', 27017)
db = connection['dawn']
def func_time(func):
    def _wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        print func.__name__,'run:',time.time()-start
    return _wrapper
@func_time
def ainsert(num):
    posts = db.userinfo
    for x in range(num):
        post = {"_id" : str(x),
        "author": str(x)+"Mike",
        "text": "My first blog post!",
        "tags": ["xiaorui", "xiaorui.cc", "rfyiamcool.51cto"],
        "date": datetime.datetime.utcnow()}
        posts.insert(post)
if __name__ == "__main__":
    #num = sys.argv[1]
    ainsert(int(1000000))
