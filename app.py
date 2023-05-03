from flask import Flask, render_template
import folium
import my_database

app = Flask(__name__)

mydb = my_database.my_client["CS4800-Project"]
mycol = mydb["Locations"]


def get_resource_locations(resource):
    res = []

    for location in mycol.find({resource: {'$exists': True}}):
        if location[resource] == True:
            location.pop("_id")
            res.append(location["name"])
    return res

@app.route("/")
def index():
    return render_template("index.html")
    
#Url that is used by script.js to obtain locations and append to list
@app.route("/getlocations/<resource>")
def get_locations(resource):
    return get_resource_locations(resource)

@app.route("/about-us")
def about():
	return render_template('about.html')

def handleMarkers(m, name, resourceVar, color, icon):

    feature_group = folium.FeatureGroup(name=name, show=False)

    for resource in mycol.find({resourceVar: {'$exists': True}}):
        if resource[resourceVar] == True:
            resource.pop("_id")
            print(resource["tooltip"])
            folium.Marker(
                location = [ resource["latitude"], resource["longitude"] ], 
                popup = resource["name"],
                tooltip=resource["tooltip"],
                icon=folium.Icon(color=color, icon=icon, prefix='fa'),
                ).add_to(feature_group)
    
    feature_group.add_to(m)

#Uses Folium to get a map location of Cal Poly Pomona
@app.route("/map")
def map():
    m = folium.Map(location=[34.05577715605838, -117.81930591750536], zoom_start=18)

    m.get_root().width = "100%"
    m.get_root().height = "600px"

    handleMarkers(m, "Buildings", "isBuilding", "cadetblue", "fa-building")
    handleMarkers(m, "Water Stations", "hasWater", "blue", "fa-tint")
    handleMarkers(m, "Bike Racks", "hasBikeRack", "green", "fa-bicycle")
    handleMarkers(m, "Printers", "hasPrinter", "black", "fa-print")
    handleMarkers(m, "Computer Lab", "hasComputerLab", "lightgray", "fa-desktop")
    handleMarkers(m, "Vending Machines", "hasVending", "purple", "fa-building")
    handleMarkers(m, "Shuttle Stop", "hasShuttleStop", "cadetblue", "fa-bus")
    handleMarkers(m, "Covid Test", "hasCovidTest", "red", "fa-medkit")
    handleMarkers(m, "Dining", "hasDining", "orange", "fa-cutlery")
    handleMarkers(m, "Library Return Drop Off Boxes", "hasLibraryReturn", "darkblue", "fa-book")
    handleMarkers(m, "Foothill Transit", "hasBusStop", "blue", "fa-bus")
    handleMarkers(m, "Electric Vehicle Charging", "hasEV", "beige", "fa-plug")
    handleMarkers(m, "Accessible Parking", "hasAccessibleParking", "blue", "fa-wheelchair")
    handleMarkers(m, "Permit Dispenser", "hasPermitDispenser", "orange", "fa-parking")
    handleMarkers(m, "Student Residence Parking", "hasResidenceParking", "darkred", "fa-parking")
    handleMarkers(m, "Student & Visitor Parking", "hasStudentParking", "darkgreen", "fa-parking")
    handleMarkers(m, "Faculty & Staff Parking", "hasFacultyParking", "cadetblue", "fa-parking")
    handleMarkers(m, "Visitor Only Parking", "hasVisitorParking", "red", "fa-parking")
    handleMarkers(m, "Motorcycle Parking", "hasMotorcycleParking", "purple", "fa-parking")
    handleMarkers(m, "Restricted Parking", "hasRestrictedParking", "black", "fa-parking")
    handleMarkers(m, "Gender Inclusive Restrooms", "hasGenderInclusiveRestroom", "black", "fa-restroom")
    handleMarkers(m, "Solar Umbrellas", "hasSolarUmbrellas", "blue", "fa-umbrella")
    handleMarkers(m, "LEED Certified Buildings", "isLeedCertifiedBuilding", "green", "fa-leaf")
    handleMarkers(m, "Solar Panels", "hasSolarPanel", "lightblue", "fa-leaf")
    handleMarkers(m, "Natural Environment", "hasNaturalEnvironment", "orange", "fa-tree")
    handleMarkers(m, "Automatic Power Door", "hasAutoPowerDoor", "blue", "fa-wheelchair")
    handleMarkers(m, "Powered Door Button", "hasPwrDoorBtn", "purple", "fa-wheelchair")
    handleMarkers(m, "Elevator", "hasElevator", "red", "fa-elevator")
    handleMarkers(m, "Athletics", "hasAthletics", "gray", "fa-life-ring")
    handleMarkers(m, "Residence", "isResidence", "darkred", "fa-building")
    handleMarkers(m, "Police and Parking Services", "isPolice", "darkpurple", "fa-bullhorn")
    handleMarkers(m, "Open Space", "isOpenSpace", "green", "fa-tree")
    handleMarkers(m, "ATMs", "hasATM", "gray", "fa-usd")
    handleMarkers(m, "Lactation Stations", "hasLactationStation", "pink", "fa-child")
    handleMarkers(m, "New Student Orientation", "hasOrientation", "purple", "fa-star")

    folium.LayerControl().add_to(m)

    iframe = m.get_root()._repr_html_()

    return render_template("map.html", iframe=iframe)

if __name__ == "__main__":
    app.run(debug=True)
