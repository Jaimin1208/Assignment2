import cherrypy
from geopy.distance import great_circle
from geopy.point import Point
import other

Item=other.connection()

class Craigslist(object):
    
    @cherrypy.expose
    def index(self):
        return "welcome"
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getsorteddata(self,criteria="price",reverse=False):
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
            
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getitem(self,id="",location=""):
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
            
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getitemslist(self,status="",userid=""):
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
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_items_in_radius(self,radius,latitude,longitude):
    
        center_point = Point(float(latitude), float(longitude)) 
        locations_within_radius = []
        for item in Item.select():
            location_coords = Point(item.latitude, item.longitude) #latitude,longitude
            distance = great_circle(center_point, location_coords).kilometers
            if distance <= float(radius):
                dicti={"id":item.id , "loc":[item.latitude,item.longitude],
                    "price":item.price,"status":item.status,"description":item.description , "userId": item.userId }
                locations_within_radius.append(dicti)

        return locations_within_radius



           
if __name__=='__main__':
    cherrypy.quickstart(Craigslist())


            
        
    
    