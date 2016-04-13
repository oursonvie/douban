# -*- coding: utf-8 -*-

# mongodb module

# import mongo driver
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()

db = client['douban_test']

def resetCollection():
    db.temp.drop()

def insert_cd(cd):
    cds = db.cd_detail    
    cd_id = cds.insert_one(cd).inserted_id
    print cd_id, cds.count()

def get_cd_urls():
    # return db.cd_detail.find({},{'link':1})
    return db.cd_detail.find()
    
def update(new_data, cd_id):
    # update existing
    update_state = db.cd_detail.update(
        {'_id':cd_id},
        {'$set':
            new_data            
        }
    )
    
    print update_state
    