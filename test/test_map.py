def test_map(app, client):
    res = client.get('/map')
    html = res.data.decode()
    assert res.status_code == 200
    assert "Home" in html
    assert "Map" in html
    assert "About" in html

def test_hasBikeRack_location(app, client):
    res = client.get('/getlocations/hasBikeRack')
    assert res.status_code == 200
    data = res.text
    assert data == (
        '["Building One","College of Agriculture","Science Laboratory","College of Letters, Arts, Social Sciences",'
        + '"College of Education and Integrative Studies","College of Environmental Design","College of Science",'
        + '"College of Engineering ","University Library"," Bronco Recreation Intramural Complex (BRIC)",'
        + '"Bronco Bookstore","Campus Center","Student Services Building"]\n'
                    ), "hasBikeRack check failed"

def test_hasWaterStation_location(app, client):
    res = client.get('/getlocations/hasWater')
    assert res.status_code == 200
    data = res.text
    assert data == (
        '["Building One","College of Agriculture","Science Laboratory","Biotechnology Building",'
        + '"College of Letters, Arts, Social Sciences","College of Education and Integrative Studies",'
        + '"College of Environmental Design","College of Science","College of Engineering ",'
        + '"Art Department and Engineering Anex","University Library","Engineering Laboratories",'
        + '"Music","Drama Department/Theatre","University Plaza","W.K. Kellogg Arabian Horse Center",'
        + '"Bronco Student Center","Darlene May Gymnasium"," Bronco Recreation Intramural Complex (BRIC)",'
        + '"Kellogg Arena","Health Services","Building 49: Training Center","Residence Suites","Residence Suites 60",'
        + '"Residence Suites 61","Residence Suites 62","Residence Suites 63","Bronco Bookstore","Procurement/Receiving",'
        + '"Collins College of Hospitality Management","Collins College of Hospitality Management","Facilities Management",'
        + '"Facilities Management Warehouse","Auto Shop","I-Poly High School","Interim Design Center: 89",'
        + '"Laboratory Facility","University Office Building","Paint Shop","Campus Center","Classroom/Laboratory/Administration (C/L/A)",'
        + '"Student Services Building","College of Business Administration: 162","College of Business Administration: 163",'
        + '"College of Business Administration: 164","Center for Regenerative Studies: 209","AGRIscapes/Farm Store"]\n'
                    ), "getlocations/hasWater check failed"


def test_isBuilding_location(app, client):
    res = client.get('/getlocations/isBuilding')
    assert res.status_code == 200
    data = res.text
    assert data == (
        '["Building One","College of Agriculture",'
        + '"Science Laboratory","Biotechnology Building","BioTrek Learning Center","College of Letters, Arts, Social Sciences",'
        + '"College of Education and Integrative Studies","College of Environmental Design","College of Science",'
        + '"College of Engineering ","Art Department and Engineering Anex","Army ROTC","Army ROTC","Pre-College TRIO Programs",'
        + '"University Library","Engineering Laboratories","Residence Hall, Encinitas","Residence Hall, Monecito","Residence Hall, Alamitos",'
        + '"Residence Hall, Aliso","Music","Temporary Classroom A","Temporary Classroom B","Temporary Classroom C",'
        + '"Temporary Classroom D","Temporary Classroom E","Drama Department/Theatre","University Plaza",'
        + '"Student Orientation Center","Fruit/Crops Unit","W.K. Kellogg Arabian Horse Center","Agriculture Unit",'
        + '"Poultry Unit/Poultry Houses","Beef Unit/Feed Shed","Feedmill","Meat Laboratory","Bronco Student Center",'
        + '"Keith and Janet Kellogg University Art Gallery","Swine Unit/Shelters","Sheep/Wool Unit",'
        + '"Darlene May Gymnasium"," Bronco Recreation Intramural Complex (BRIC)","Kellogg Arena","Swimming Pool",'
        + '"Apparel Merchandising and Management","Health Services","Agricultural Engineering Tractor Shop","Custodial Offices",'
        + '"Building 49: Training Center","Vista Market","Residence Suites","Foundation Administration Offices","Storage Building",'
        + '"Residence Hall, Palmitas","Residence Hall, Cedritos","La Cienega Center (University Housing Services)","Residence Suites 60",'
        + '"Residence Suites 61","Residence Suites 62","Residence Suites 63","Rose Float Laboratory","Pesticide Building","Bronco Bookstore","Hay Barn",'
        + '"Los Olivos Commons","Recreation/Maintenance","Centerpointe Dining Commons","Residence Suites, Sicomoro Hall","Residence Suites",'
        + '"Procurement/Receiving","Kellogg West Education/Dining","Kellogg West/Addition","Kellogg West Main Lodge","Kellogg West Addition",'
        + '"Collins College of Hospitality Management","Collins College of Hospitality Management","Collins College of Hospitality Management",'
        + '"Collins College of Hospitality Management","Facilities Management","Environmental Health and Safety","Facilities Management Warehouse",'
        + '"Carpenter Shop","Auto Shop","I-Poly High School","English Language Institute: 86","English Language Institute: 86A","English Language Institute: 86B",'
        + '"English Language Institute: 86C","Interim Design Center: 89","Interim Design Center: 89A","Interim Design Center: 89B","Medic-1",'
        + '"Information Technology & Institutional Planning","Laboratory Facility","University Office Building","Cultural Centers","Paint Shop",'
        + '"Campus Center","Classroom/Laboratory/Administration (C/L/A)","CLA Classrooms","CLA Paseo","Storage Building: 99","Storage Building: 109",'
        + '"Police and Parking Services","Manor House","Kellogg House Pomona","Guest House","Child Care Center","Student Services Building",'
        + '"College of Business Administration: 162","College of Business Administration: 163","College of Business Administration: 164","Chilled Water Center Plant",'
        + '"University Village","John T. Lyle Center for Regenerative Studies","Center for Regenerative Studies: 209","John T. Lyle Center for Regenerative Studies: 209C",'
        + '"John T. Lyle Center for Regenerative Studies: 209L","John T. Lyle Center for Regenerative Studies: 209R","John T. Lyle Center for Regenerative Studies: 209S",'
        + '"John T. Lyle Center for Regenerative Studies: 209W","John T. Lyle Center for Regenerative Studies: 210","AGRIscapes/Farm Store","AGRIscapes","Edison SCE2",'
        + '"Innovation Village SCE","American Red Cross Headquarters","Edison SCE1","Center for Training, Technology, and Incubation: 220A",'
        + '"Center for Training, Technology, and Incubation: 220B","Center for Training, Technology, and Incubation: 220C"]\n'
        ), 'getlocations/isBuilding check has failed'
    
def test_hasPrinter_location(app, client):
    res = client.get('/getlocations/hasPrinter')
    assert res.status_code == 200
    data = res.text
    assert data == (
        '["Building One","College of Agriculture","Biotechnology Building","College of Science","College of Engineering ","University Library","24 Hour Computer Lab","Engineering Laboratories","Drama Department/Theatre","Apparel Merchandising and Management","Collins College of Hospitality Management","Interim Design Center: 89","Campus Center"]\n'
    ), 'getlocations/hasPrinter check has failed'

def test_hasComputerLab_location(app, client):
	res = client.get('/getlocations/hasComputerLab')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Building One","College of Agriculture","Biotechnology Building","College of Science","College of Engineering ","University Library","24 Hour Computer Lab","Engineering Laboratories","Drama Department/Theatre","Apparel Merchandising and Management","Collins College of Hospitality Management","Interim Design Center: 89","Campus Center"]\n'
	), 'getlocations/hasComputerLab check has failed'
        
def test_hasVending_location(app, client):
	res = client.get('/getlocations/hasVending')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Building One","College of Agriculture","Science Laboratory","Biotechnology Building","College of Letters, Arts, Social Sciences","College of Science","College of Engineering ","Art Department and Engineering Anex","Music","Drama Department/Theatre","Bronco Student Center","Darlene May Gymnasium","Kellogg Arena","Apparel Merchandising and Management","Residence Suites 60","Residence Suites 61","Bronco Bookstore","Collins College of Hospitality Management","Interim Design Center: 89","Campus Center","Classroom/Laboratory/Administration (C/L/A)"]\n'
	), 'getlocations/hasVending check has failed'
        
def test_hasShuttleStop_location(app, client):
	res = client.get('/getlocations/hasShuttleStop')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Shuttle Stop: Building 7","Shuttle Stop: Lot L","Shuttle Stop: Building 94","Shuttle Stop: Building 58","Shuttle Stop: Building 91","Shuttle Stop: Parking Structure 1","Shuttle Stop: Building 121","Shuttle Stop: Building 89","Shuttle Stop: Lot B","Shuttle Stop: S Campus Dr","Shuttle Stop: AGRIscapes","Shuttle Stop: S University Dr 1","Shuttle Stop: S University Dr 2","Shuttle Stop: Parking Structure 2"]\n'
	), 'getlocations/hasShuttleStop check has failed'
        
def test_hasCovidTest_location(app, client):
	res = client.get('/getlocations/hasCovidTest')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Bronco Student Center","Residence Suites"]\n'
	), 'getlocations/hasCovidTest check has failed'
        
def test_hasDining_location(app, client):
	res = client.get('/getlocations/hasDining')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["College of Environmental Design","University Library","Bronco Student Center"," Bronco Recreation Intramural Complex (BRIC)","Vista Market","Centerpointe Dining Commons","Kellogg West Education/Dining","Collins College of Hospitality Management","Campus Center","Innovation Brew Works","Farm Store","Element Coffee & Food","Carl\'s Jr","ENV Cafe","Farm Store","Fresh Escapes","International Grounds","Jamba Juide - BRIC","Jamba Juice Express","Kellogg West Dining","Panda Express","Poly Fresh Market","Pony Express - CBA","Pony Express - CCMP","Pony Express - CLA","Qdoba","Restaurant at Kellogg Ranch","Round Table Pizza","Starbucks","Subway"]\n'
	), 'getlocations/hasDining check has failed'
        
def test_hasLibraryReturn_location(app, client):
	res = client.get('/getlocations/hasLibraryReturn')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["University Library","Bronco Bookstore","Drive-By Drop Return for Library Books"]\n'
	), 'getlocations/hasLibraryReturn check has failed'
	
def test_hasBusStop_location(app, client):
	res = client.get('/getlocations/hasBusStop')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Foothill Transit ID:2565","Foothill Transit ID:2564","Foothill Transit ID:2563","Foothill Transit ID:2322","Foothill Transit ID:2562","Foothill Transit ID:2566","Foothill Transit ID:2567","Foothill Transit ID:2631","Foothill Transit ID:3141","Foothill Transit ID:3140","Foothill Transit"]\n'
	), 'getlocations/hasBusStop check has failed'
	
def test_hasEV_location(app, client):
	res = client.get('/getlocations/hasEV')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Parking Structure 2","Parking Structure B","Parking Structure H","Parking Structure Q","Parking Lot L"]\n'
	), 'getlocations/hasEV check has failed'
	
def test_hasAccessibleParking_location(app, client):
	res = client.get('/getlocations/hasAccessibleParking')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Accessible Parking: 1","Accessible Parking: 2","Accessible Parking: A","Accessible Parking: C","Accessible Parking: E1","Accessible Parking: E2","Accessible Parking: F4","Accessible Parking: F8","Accessible Parking: G","Accessible Parking: J","Accessible Parking: K","Accessible Parking: L","Accessible Parking: M","Accessible Parking: Camphor/Olive","Accessible Parking: University Dr/University Quad","Accessible Parking: S University Dr/Olive Lane Walk"]\n'
	), 'getlocations/hasAccessibleParking check has failed'
	
def test_hasPermitDispenser_location(app, client):
	res = client.get('/getlocations/hasPermitDispenser')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Permit Dispenser: 1","Permit Dispenser: 2","Permit Dispenser: B1","Permit Dispenser: B2","Permit Dispenser: C","Permit Dispenser: E2","Permit Dispenser: Express Lot","Permit Dispenser: F5","Permit Dispenser: G","Permit Dispenser: J","Permit Dispenser K","Permit Dispenser: M1","Permit Dispenser: M2","Permit Dispenser: U","Permit Dispenser: Village","Permit Dispenser: Info Booth","Permit Dispenser: Kellogg Field"]\n'
	), 'getlocations/hasPermitDispenser check has failed'
	
def test_hasResidenceParking_location(app, client):
	res = client.get('/getlocations/hasResidenceParking')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Parking Residence: F2","Parking Residence: P","Parking Residence: Q"]\n'
	), 'getlocations/hasResidenceParking check has failed'
	
def test_hasStudentParking_location(app, client):
	res = client.get('/getlocations/hasStudentParking')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Student Parking: 1","Student Parking: 2","Student Parking: B","Student Parking: E1","Student Parking: E2","Student Parking: F1","Student Parking: F3","Student Parking F5","Student Parking: F9","Student Parking: F10","Student Parking: J3-J4","Student Parking: J5-J8","Student Parking: K","Student Parking: M","Student Parking: T","Student Parking: U","Student Parking: Kellogg House","Student Parking: Overflow Parking","Student Parking: Overflow Parking"]\n'
	), 'getlocations/hasStudentParking check has failed'
	
def test_hasFacultyParking_location(app, client):
	res = client.get('/getlocations/hasFacultyParking')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Faculty and Staff Parking: A","Faculty and Staff Parking: F4","Faculty and Staff Parking: F8","Faculty and Staff Parking: J1-J2","Faculty and Staff Parking: L","Faculty and Staff Parking: M","Faculty and Staff Parking: O","Faculty and Staff Parking: S"]\n'
	), 'getlocations/hasFacultyParking check has failed'

def test_hasVisitorParking_location(app, client):
	res = client.get('/getlocations/hasVisitorParking')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Visitor Only Parking: I","Visitor Only Parking"]\n'
	), 'getlocations/hasVisitorParking check has failed'
	
def test_hasMotorcycleParking_location(app, client):
	res = client.get('/getlocations/hasMotorcycleParking')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Motorcycle Parking: J2","Motorcycle Parking: S University Dr","Motorcycle Parking: S University Dr","Motorcycle Parking Lot F4","Motorcycle Parking: 1","Motorcycle Parking: B"]\n'
	), 'getlocations/hasMotorcycleParking check has failed'
	
def test_hasRestrictedParking_location(app, client):
	res = client.get('/getlocations/hasRestrictedParking')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Restricted Parking: G"]\n'
	), 'getlocations/hasRestrictedParking check has failed'
	
def test_hasGenderInclusiveRestroom_location(app, client):
	res = client.get('/getlocations/hasGenderInclusiveRestroom')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["BioTrek Learning Center","College of Environmental Design","University Library","Residence Hall, Encinitas","Residence Hall, Monecito","Residence Hall, Alamitos","Residence Hall, Aliso","Music","University Plaza","W.K. Kellogg Arabian Horse Center","Agriculture Unit","Beef Unit/Feed Shed","Bronco Student Center","Swine Unit/Shelters","Sheep/Wool Unit"," Bronco Recreation Intramural Complex (BRIC)","Apparel Merchandising and Management","Health Services","Vista Market","Residence Suites","Residence Suites 60","Residence Suites 61","Residence Suites 62","Residence Suites 63","Los Olivos Commons","Information Technology & Institutional Planning","University Office Building","Cultural Centers","Police and Parking Services","Student Services Building","College of Business Administration: 164","Chilled Water Center Plant","University Village"]\n'
	), 'getlocations/hasGenderInclusiveRestroom check has failed'
	
def test_hasSolarUmbrellas_location(app, client):
	res = client.get('/getlocations/hasSolarUmbrellas')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Solar Umbrella","Solar Umbrella"]\n'
	), 'getlocations/hasSolarUmbrellas check has failed'
	
def test_isLeedCertifiedBuilding_location(app, client):
	res = client.get('/getlocations/isLeedCertifiedBuilding')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'[" Bronco Recreation Intramural Complex (BRIC)","Residence Suites","Residence Suites 60","Residence Suites 61","Residence Suites 62","Residence Suites 63","Centerpointe Dining Commons","Residence Suites, Sicomoro Hall","Residence Suites","Collins College of Hospitality Management","I-Poly High School","Student Services Building","College of Business Administration: 162","College of Business Administration: 163","College of Business Administration: 164","Edison SCE2","Innovation Village SCE","Edison SCE1"]\n'
	), 'getlocations/isLeedCertifiedBuilding check has failed'
	
def test_hasSolarPanel_location(app, client):
	res = client.get('/getlocations/hasSolarPanel')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Kellogg Arena","John T. Lyle Center for Regenerative Studies","Student Parking: 2","Student Parking: M"]\n'
	), 'getlocations/hasSolarPanel check has failed'
	
def test_hasNaturalEnvironment_location(app, client):
	res = client.get('/getlocations/hasNaturalEnvironment')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["BioTrek Learning Center","W.K. Kellogg Arabian Horse Center","Center for Regenerative Studies: 209","AGRIscapes","Solar Umbrella","BioTrek Ethnobotany Garden","Mesozoic Garden","Voorhis Ecological Reserve","Aratani Japanese Garden","Rose Garden"]\n'
	), 'getlocations/hasNaturalEnvironment check has failed'
	
def test_hasAutoPowerDoor_location(app, client):
	res = client.get('/getlocations/hasAutoPowerDoor')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Building One","College of Agriculture","Science Laboratory","College of Letters, Arts, Social Sciences","College of Education and Integrative Studies","College of Environmental Design","College of Science","College of Engineering ","University Library","Music","Health Services","Residence Suites, Sicomoro Hall","Residence Suites","Collins College of Hospitality Management","Campus Center","Student Services Building","College of Business Administration: 163","College of Business Administration: 164"]\n'
	), 'getlocations/hasAutoPowerDoor check has failed'
	
def test_hasPwrDoorBtn_location(app, client):
	res = client.get('/getlocations/hasPwrDoorBtn')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Science Laboratory","College of Letters, Arts, Social Sciences","College of Education and Integrative Studies","College of Science","College of Engineering ","Engineering Laboratories","Bronco Student Center"," Bronco Recreation Intramural Complex (BRIC)","Bronco Bookstore","Centerpointe Dining Commons","Police and Parking Services","College of Business Administration: 164"]\n'
	), 'getlocations/hasPwrDoorBtn check has failed'
	
def test_hasElevator_location(app, client):
	res = client.get('/getlocations/hasElevator')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Building One","College of Agriculture","Science Laboratory","Biotechnology Building","College of Letters, Arts, Social Sciences","College of Education and Integrative Studies","College of Environmental Design","College of Science","College of Engineering ","Art Department and Engineering Anex","University Library","Engineering Laboratories","Music","Bronco Student Center"," Bronco Recreation Intramural Complex (BRIC)","Bronco Bookstore","Residence Suites, Sicomoro Hall","Residence Suites","Collins College of Hospitality Management","University Office Building","Police and Parking Services","Student Services Building","College of Business Administration: 163","College of Business Administration: 164"]\n'
	), 'getlocations/hasElevator check has failed'
	
def test_hasAthletics_location(app, client):
	res = client.get('/getlocations/hasAthletics')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Darlene May Gymnasium","Kellogg Arena","Kellogg Track and Field","Scolinos Baseball Field","Soccer Field","Tennis Courts"]\n'
	), 'getlocations/hasAthletics check has failed'
	
def test_isResidence_location(app, client):
	res = client.get('/getlocations/isResidence')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Residence Hall, Encinitas","Residence Hall, Monecito","Residence Hall, Alamitos","Residence Hall, Aliso","Residence Suites","Residence Hall, Palmitas","Residence Hall, Cedritos","Residence Suites 60","Residence Suites 61","Residence Suites 62","Residence Suites 63","Residence Suites, Sicomoro Hall","Residence Suites","University Village"]\n'
	), 'getlocations/isResidence check has failed'
	
def test_isPolice_location(app, client):
	res = client.get('/getlocations/isPolice')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Police and Parking Services"]\n'
	), 'getlocations/isPolice check has failed'
	
def test_isOpenSpace_location(app, client):
	res = client.get('/getlocations/isOpenSpace')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["BioTrek Ethnobotany Garden","Voorhis Ecological Reserve","Aratani Japanese Garden","Rose Garden","Bronco Commons","University Park","University Quad","Kellogg Track and Field","Scolinos Baseball Field","Soccer Field","Tennis Courts","AGRIsacpes Pumpkin Field","Engineering Meadow (Open Space)","Outdoor Basketball Court","Spadra Farm","Voorhis Park"]\n'
	), 'getlocations/isOpenSpace check has failed'
	
def test_hasATM_location(app, client):
	res = client.get('/getlocations/hasATM')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Bronco Student Center"]\n'
	), 'getlocations/hasATM check has failed'
	
def test_hasLactationStation_location(app, client):
	res = client.get('/getlocations/hasLactationStation')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["Health Services","Bronco Bookstore","Collins College of Hospitality Management","Cultural Centers","Student Services Building"]\n'
	), 'getlocations/hasLactationStation check has failed'
	
def test_hasOrientation_location(app, client):
	res = client.get('/getlocations/hasOrientation')
	assert res.status_code == 200
	data = res.text
	assert data == (
        	'["College of Engineering ","University Library","Drama Department/Theatre","University Plaza","Bronco Student Center"," Bronco Recreation Intramural Complex (BRIC)","Bronco Bookstore","Centerpointe Dining Commons","Cultural Centers","Student Services Building","Student Parking: 2","Bronco Commons","New Student Orientation","University Park","University Quad"]\n'
	), 'getlocations/hasOrientation check has failed'