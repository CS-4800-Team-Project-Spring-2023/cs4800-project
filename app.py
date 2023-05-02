from flask import Flask, render_template
import folium
import my_database
import pandas as pd
import pytest

app = Flask(__name__)

mydb = my_database.my_client["CS4800-Project"]
mycol = mydb["Locations"]


def get_resource_locations(location):
    res = []

    if location == "water_station":
        for location in mycol.find():
            if location["hasWater"] == True:
                location.pop("_id")
                res.append(location["name"])
        return res
    elif location == "bike_rack":
        for location in mycol.find():
            if location["hasBikeRack"] == True:
                location.pop("_id")
                res.append(location["name"])
        return res
    elif location == "printer":
        for location in mycol.find():
            if location["hasPrinter"] == True:
                location.pop("_id")
                res.append(location["name"])
        return res

# basic helper function for use in the pytest route
def pytest_test(num):
    return pow(num, 2)

@app.route("/")
def index():
    return render_template("index.html")
    
#Url that is used by script.js to obtain locations and append to list
@app.route("/getlocations/<location>")
def get_locations(location):
    return get_resource_locations(location)

@app.route("/about-us")
def about():
	return render_template('about.html')

def handleMarkers(resourceName, fg, colorName, icon):
    for resource in mycol.find({resourceName: {'$exists': True}}):
        if resource[resourceName] == True:
            resource.pop("_id")
            print(resource["tooltip"])
            folium.Marker(
                location = [ resource["latitude"], resource["longitude"] ], 
                popup = resource["name"],
                tooltip=resource["tooltip"],
                icon=folium.Icon(color=colorName, icon=icon, prefix='fa'),
                ).add_to(fg)

# Use folium.Marker to group the resources to a specific category
def createFeatureGroups(m): 
    feature_group1 = folium.FeatureGroup(name="Water Stations", show=False)
    feature_group2 = folium.FeatureGroup(name="Bike Racks", show=False)
    feature_group3 = folium.FeatureGroup(name="Printers", show=False)
    feature_group4 = folium.FeatureGroup(name="Vending Machines", show=False)
    feature_group5 = folium.FeatureGroup(name="ATMs", show=False)
    feature_group6 = folium.FeatureGroup(name="Covid Test", show=False)
    feature_group7 = folium.FeatureGroup(name="Dining", show=False)
    feature_group8 = folium.FeatureGroup(name="Library Return Drop Off Boxes", show=False)
    feature_group9 = folium.FeatureGroup(name="Foothill Transit", show=False)
    feature_group10 = folium.FeatureGroup(name="Electric Vehicle Charging", show=False)
    feature_group11 = folium.FeatureGroup(name="Accessible Parking", show=False)

    handleMarkers("hasWater", feature_group1, "blue", "fa-tint")
    handleMarkers("hasBikeRack", feature_group2, "green", "fa-bicycle")
    handleMarkers("hasPrinter", feature_group3, "black", "fa-print")
    handleMarkers("hasVending", feature_group4, "purple", "fa-building")
    handleMarkers("hasATM", feature_group5, "gray", "fa-usd")
    handleMarkers("hasCovidTest", feature_group6, "red", "fa-medkit")
    handleMarkers("hasDining", feature_group7, "orange", "fa-cutlery")
    handleMarkers("hasLibraryReturn", feature_group8, "darkblue", "fa-book")
    handleMarkers("hasBusStop", feature_group9, "blue", "fa-bus")
    handleMarkers("hasEV", feature_group10, "beige", "fa-plug")
    handleMarkers("hasAccessibleParking", feature_group11, "lightblue", "fa-wheelchair")

    feature_group1.add_to(m)
    feature_group2.add_to(m)
    feature_group3.add_to(m)
    feature_group4.add_to(m)
    feature_group5.add_to(m)
    feature_group6.add_to(m)
    feature_group7.add_to(m)
    feature_group8.add_to(m)
    feature_group9.add_to(m)
    feature_group10.add_to(m)
    feature_group11.add_to(m)
    folium.LayerControl().add_to(m)

#Uses Folium to get a map location of Cal Poly Pomona
@app.route("/map")
def map():
    m = folium.Map(location=[34.05577715605838, -117.81930591750536], zoom_start=18)

    m.get_root().width = "800px"
    m.get_root().height = "600px"

    createFeatureGroups(m)

    iframe = m.get_root()._repr_html_()

    return render_template("map.html", iframe=iframe)

@app.route("/CS4800")
def CS4800():
    return "Welcome CS4800 to our CPP Map Finder application!"

@app.route("/pandas")
def pnd():
    df = pd.DataFrame({ "Project": ["CPP", "Map", "Finder"]})
    return df.to_string(index=False)
    
@app.route("/pytest")
def test_pytest():
    assert pytest_test(5) == 25
    return "CPP Map Finder could benefit from the usage of Pytest."

@app.route("/Disclaimer")
def disclaimer():
    return "This application is a work in progress and is currently not a representation of the final product."

if __name__ == "__main__":
    app.run(debug=True)
