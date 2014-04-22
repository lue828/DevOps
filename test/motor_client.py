import motor

uri = 'mongodb://127.0.0.1/my_database'
client = MotorClient(uri)
db = client.get_default_database()
assert db.name == 'my_database'