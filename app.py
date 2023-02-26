from flask import Flask, render_template
import folium
import pymongo

app = Flask(__name__)


#establish database connection using pymongo
my_client = pymongo.MongoClient("***")

mydb = my_client["CS4800-Project"]
mycol = mydb["Locations"]



#For now, just returns all locations with hydration states. Can't filter or interact with frontend, mostly just to
#test database connection
@app.route("/")
def get_locations():
    res = []
    for location in mycol.find():
         if location["hasWater"] == True:
              location.pop("_id")
              res.append(location["name"])
    return res

@app.route("/about-us")
def about():
	return render_template('index.html')

#Uses Folium to get a map location of Cal Poly Pomona
@app.route("/map")
def map():
    m = folium.Map(location=[34.05577715605838, -117.81930591750536], zoom_start=18)
    return m.get_root().render()

@app.route("/CS4800")
def CS4800():
    return "Welcome CS4800 to our CPP Map Finder application!"

@app.route("/Disclaimer")
def disclaimer():
    return "This application is a work in progress and is currently not a representation of the final product."

if __name__ == "__main__":
    app.run(debug=True)
