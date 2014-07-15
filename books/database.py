#-*- coding: utf-8 -*-
from pymongo import Connection

class database():
    conn = Connection('172.16.27.27', 27017)
    db = conn['test']
    @classmethod
    def getDB(cls):
        return cls.db