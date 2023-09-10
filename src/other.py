from peewee import *
import json


filee=open("../data/data.json")
filee=json.load(filee)  
def connection():

    db = SqliteDatabase('Craigslist.db')
    class Item(Model):
        id=TextField(primary_key=True)
        latitude=FloatField()
        longitude=FloatField()
        userId=CharField()
        description=CharField(null=True)
        price=IntegerField()
        status=CharField()

        class Meta:
            database = db 

    db.connect()

    #inserting into database

    db.create_tables([Item])
    # for element in filee:
    #     Item.create(id=element["id"] , latitude=element["loc"][0], longitude=element["loc"][1],userId=element["userId"], 
    #                 description=element["description"] , price=element["price"] ,status=element["status"])

    return Item   
# connection() 
