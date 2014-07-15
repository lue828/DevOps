#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json
from db import database

db = database.database.getDB()

host = db.host.find_one({'hid':hostname})
server = db.server.find_one({'sid':server})