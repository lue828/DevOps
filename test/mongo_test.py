#!/usr/bin/env python

import pymongo

conn = pymongo.Connection('127.0.0.1', 27017)
db = conn.monitor
stat = db.stat

#for s in stat.find():
#    print s

#print stat.find().count()

db2 = conn.testdb
test = db2.test
for i in xrange(100000, 1000001):
    test.insert({"id": i, "name": "dawn", "addr": "Shanghai pudong", "country": "China"})
