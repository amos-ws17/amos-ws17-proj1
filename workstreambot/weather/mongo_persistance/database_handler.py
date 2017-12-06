from pymongo import MongoClient


class MongoDBHandler:


    def __init__(self, mongo_ip="localhost", mongo_port=27017):
        self.mongo_ip = mongo_ip
        self.mongo_port = mongo_port
        self.client =  MongoClient(mongo_ip, mongo_port)

    def get_client(self):
        return self.client

    def write_data(self, data, collection_name, db_name):

        db = self.client[db_name]
        collection = db.get_collection(collection_name)
        collection.insert_one(data)

    def find_in_collection(self, key, collection_name, db_name):
        db = self.client[db_name]
        collection = db.get_collection(collection_name)
        objs = collection.find(key).sort("name")
        return objs

    def find_one_in_collection(self, key, collection_name, db_name):
        db = self.client[db_name]
        collection = db.get_collection(collection_name)
        obj = collection.find_one(key)
        return obj

    def find_all_in_collection(self, collection_name, db_name):
        db = self.client[db_name]
        collection = db.get_collection(collection_name)
        all = collection.find()
        return all

    def get_collection_size(self, collection_name, db_name):
        db = self.client[db_name]
        collection = db.get_collection(collection_name)
        return collection.find({}).count()
