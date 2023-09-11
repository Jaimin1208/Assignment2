# Cragislist API server

## synopsis
The API extracts information regarding items listed for sale on craigslist.

The API is made using _cherrypy api_ in **phase1** branch.

_Peewee_ is used as ORM for mapping **data.json** with **sqliteDB** in **phase2** branch.

The API is made using _FASTAPI_ in **phase3** branch.

## Getting Started:
1. Clone the repository.
2. Install dependencies from **requirements.txt** using :
   ```
   python install -r requirements.txt
   ```
3. Run **python app.py** file after navigating into _Assignment2/src_ directory.

## API EndPoints:
1. The entire list sorted by the item’s price (Ascending and Descending) -
```
getsorteddata?reverse=True&criteria=price
```
2. Any single item by:
```
a. Id - getitem?id=AAsm
b. Location - getitem?location=AAsm
```
3. List of items by:
```
a. Status - getitemslist?status=AAsm
b. userId - getitemslist?userid=AAsm
```
4. An array of items based on radius:
```
Location specified by coordinate - get_items_in_radius?radius=xy&latitude=xx&longitude=yy
```

## Acknowledgments:
**cherrypy**
**peewee**
**geopy**
**fastapi**
**uvicorn**




