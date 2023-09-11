from fastapi import FastAPI
import uvicorn

from geopy.distance import great_circle
from geopy.point import Point
import other

Item=other.connection()

app = FastAPI()


@app.get("/")
def root():
    return {"message": "welcome"}
   
@app.get("/getsorteddata")
def getsorteddata(criteria:str ="price",reverse:bool =False):
    if reverse==False:
        query=Item.select().order_by(Item.price) 
    else:
        query=Item.select().order_by(Item.price.desc()) 

    output=[]
    for item in query:
        dicti={"id":item.id , "loc":[item.latitude,item.longitude],
                "price":item.price,"status":item.status,"description":item.description , "userId": item.userId }
        output.append(dicti)
    return output
        
    
@app.get("/getitem")
def getitem(id:str="",location:str=""):
    if id !="":
        item=Item.get(Item.id ==  id)
        dicti={"id":item.id , "loc":[item.latitude,item.longitude],
                "price":item.price,"status":item.status,"description":item.description , "userId": item.userId }
        return [dicti]

    elif location !="":    
        location=location.split(",")
        item=Item.get((Item.latitude==float(location[0])) & (Item.longitude==float(location[1])))
        dicti={"id":item.id , "loc":[item.latitude,item.longitude],
                "price":item.price,"status":item.status,"description":item.description , "userId": item.userId }
        return [dicti]
            
@app.get("/getitemslist")
def getitemslist(status:str="",userid:str=""):
    output=[]
    if status!="":
        query= Item.select().where(Item.status == status)
    elif userid!="":
        query = Item.select().where(Item.userId==userid)
    for item in query:
        dicti={"id":item.id , "loc":[item.latitude,item.longitude],
                "price":item.price,"status":item.status,"description":item.description , "userId": item.userId }
        output.append(dicti)

    return output

@app.get("/get_items_in_radius")
def get_items_in_radius(radius:float,latitude:float,longitude:float):

    center_point = Point((latitude), (longitude)) 
    locations_within_radius = []
    for item in Item.select():
        location_coords = Point(item.latitude, item.longitude) #latitude,longitude
        distance = great_circle(center_point, location_coords).kilometers
        if distance <= (radius):
            dicti={"id":item.id , "loc":[item.latitude,item.longitude],
                "price":item.price,"status":item.status,"description":item.description , "userId": item.userId }
            locations_within_radius.append(dicti)

    return locations_within_radius

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=10001)


           



            
        
    
    