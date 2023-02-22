from pymongo import MongoClient

client = MongoClient('localhost', 27017)

Database = client.get_database('local')

Table = Database['Ukraine migration']

cursor = Table.find()
