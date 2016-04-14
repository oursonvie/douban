# -*- coding: utf-8 -*-

# i'm writing this script to make a copy of an entire mongodb
# this copy is happending within same database, therefore an copy of collections

# import mongo driver
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()

# set database
db = client['douban_test']

# set collection
fromDB = db.cd_detail
toDB = db.cd_copy

def copyDataBase():
    cds = fromDB.find()
    for cd in cds:
        toDB.insert_one(cd)
        print toDB.count()
        
def makeThemNumber():
    cds = toDB.find()
    for cd in cds:
        _id = cd['_id']
        
        # convert douban_score into float
        try:
            douban_score = float(cd['douban_score'])
        except:
            douban_score = cd['douban_score']
        # convert people_voted into int
        try:
            people_voted = int(cd['people_voted'])
        except:
            people_voted = cd['people_voted']
        # print _id, type(douban_score), douban_score, type(people_voted), people_voted
        
        update_state = toDB.update(
            {'_id':_id},
            {'$set':
             {
                'douban_score': douban_score,
                'people_voted': people_voted
                    }
            }
        )
        
        print update_state

def checkUpdate():
    cds = toDB.find()
    for cd in cds:
        _id = cd['_id']
        douban_score = cd['douban_score']
        people_voted = cd['people_voted']
        
        print _id, type(douban_score), douban_score, type(people_voted), people_voted

        
def main():
    # copyDataBase()
    # makeThemNumber()

    # check the updated data is now numbers
    checkUpdate()
    
if __name__ == "__main__":
    main()