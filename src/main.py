import cherrypy
import json

from geopy.distance import great_circle
from geopy.point import Point


class Craigslist(object):

    def openfile(self):
        filee=open("data.json")
        return json.load(filee)
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return self.openfile()
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getsorteddata(self,criteria="price",reverse=False):
        sorteddata=sorted(self.openfile(), key=lambda item:item[criteria],reverse=bool(reverse))
        return sorteddata
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getitem(self,id="",location=""):
        filee=self.openfile()
        for item in filee:
            if item["id"]==id:
                return [item]
            
        location=location.split(",")
        location=[float(item) for item in location]
        for item in filee:
            if item["loc"]==location:
                return [item]
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getitemslist(self,status="",userid=""):
        filee=self.openfile()
        output=[]
        for item in filee:
            if item["status"]==status:
                output.append(item)

        for item in filee:
            if item["userId"]==userid:
                output.append(item)
        return output
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_items_in_radius(self,radius,latitude,longitude):
        filee=self.openfile()
    
        center_point = Point(float(latitude), float(longitude)) 
        locations_within_radius = []
        for item in filee:
            location_coords = Point(item["loc"][0], item["loc"][1]) #latitude,longitude
            distance = great_circle(center_point, location_coords).kilometers
            if distance <= float(radius):
                locations_within_radius.append(item)

        return locations_within_radius










            

            
            
        

        

    




           
if __name__=='__main__':
    cherrypy.quickstart(Craigslist())


            
        
    
    