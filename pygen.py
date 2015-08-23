import random
import json

def random_coordinates_inc(prev_x,prev_y):
    """Generate a positive coordinate"""
    x_coord = random.uniform(prev_x + 0, prev_x + 15)
    x_coord = round(x_coord, 4)
    if x_coord > 15:
        x_coord = 15
    if x_coord < -15:
        x_coord = -15
    y_coord = random.uniform(prev_y + 0, prev_y + 15)
    y_coord = round(y_coord, 4)
    if y_coord > 15:
        y_coord = 15
    if y_coord < -15:
        y_coord = -15
    return {"x": x_coord, "y": y_coord}

def random_coordinates_dec(prev_x,prev_y):
    """Generate a negative coordinate"""
    x_coord = random.uniform(prev_x + 0, prev_x - 15)
    x_coord = round(x_coord, 4)
    if x_coord > 15:
        x_coord = 15
    if x_coord < -15:
        x_coord = -15
    y_coord = random.uniform(prev_y + 0, prev_y - 15)
    y_coord = round(y_coord, 4)
    if y_coord > 15:
        y_coord = 15
    if y_coord < -15:
        y_coord = -15
    return {"x": x_coord, "y": y_coord}

def random_name():
    """Generate a random name from a list"""
    city_list = ["Capital","Awesome","Test","Concept"]
    selection = random.choice(city_list)
    return {"name": selection}

def export_geojson(dictIn, outFile):
    """Write to file"""
    json.dump(dictIn,open(outFile,"w+"), sort_keys=True, indent=4, separators=(',', ': '))

def map_setup():
    """Set up the map"""
    basemap = gen_basemap()
    # Set basemap as one of several features:
    finalMap = {}
    finalMap['type'] = 'FeatureCollection'
    finalMap['features'] = []
    finalMap['features'].append(basemap)
    return finalMap

def gen_basemap():
    """Generate the base map"""
    basemap = {}
    basemap["type"] = "Feature"
    basemap["_id"] = "fifth_world"
    basemap["properties"] = {}
    basemap["properties"]["name"] = "5th World"
    basemap["properties"]["code"] = "5WRL"
    basemap["properties"]["group"] = "Countries"
    basemap["geometry"] = {}
    basemap["geometry"]["type"] = "Polygon"
    basemap["geometry"]["coordinates"] = []
    iter_max = random.randint(10,50)
    iter_position = 0
    listFeatures = []
    firstList = []
    prev_x = random_coordinates_inc(0,0)['x']
    firstList.append(int(prev_x))
    prev_y = random_coordinates_inc(0,0)['y']
    firstList.append(int(prev_y))
    listFeatures.append(firstList)
    while iter_position != iter_max:
        new_x = random_coordinates_inc(prev_x, prev_y)['x']
        new_y = random_coordinates_inc(prev_x, prev_y)['y']
        new_list = [abs(new_x), abs(new_y)]
        if new_list not in listFeatures:
            listFeatures.append(new_list)
        prev_x = int(new_x)
        prev_y = int(new_y)
        iter_position = iter_position + 1
    iter_position = 0
    while iter_position != iter_max:
        new_x = random_coordinates_dec(prev_x, prev_y)['x']
        new_y = random_coordinates_dec(prev_x, prev_y)['y']
        new_list = [new_x, new_y]
        if new_list not in listFeatures:
            listFeatures.append(new_list)
        prev_x = int(new_x)
        prev_y = int(new_y)
        iter_position = iter_position + 1
    listFeatures.append(listFeatures[0])
    basemap["geometry"]["coordinates"].append(listFeatures)
    return basemap

def gen_lister(minLength, maxLength):
    """Generate a list of 1s, with a random length between the given ranges"""
    if type(minLength) != int:
        raise OSError
    if type(maxLength) != int:
        raise OSError
    listLength = random.randint(minLength, maxLength)
    listerList = []
    count = 0
    while count != listLength:
        listerList.append(1)
        count = count + 1
    return listerList

def main():
    """Build the map"""
    finalMap = map_setup()
    # Determine the number of Large Cities we'll have, there has to be at least one.
    LargeCities = gen_lister(1, 10)
    print(str(len(LargeCities)) + " Large Cities.")
    # Randomly choose one of the Large Cities to be the capital.

    # Determine the number of Small Cities we'll have.
    SmallCities = gen_lister(0, 20)
    print(str(len(SmallCities)) + " Small Cities.")
    # Determine the number of Villages we'll have.
    villages = gen_lister(0, 50)
    print(str(len(villages)) + " Villages.")
    # Determine the number of Ruins we'll have.
    ruins = gen_lister(0, 20)
    print(str(len(ruins)) + " Ruins.")
    # Assign a location to the Capital City.
    capitalCityFeature = {'type':'Feature', 'properties':{'name':random_name()['name'],'code':'CAP','group':'Capitals'}}
    capitalCityFeature['geometry'] = {}
    capitalCityFeature['geometry']['type'] = 'Point'
    capitalCityFeature['geometry']['coordinates'] = []
    capitalCityFeature['geometry']['coordinates'].append(random_coordinates_inc(0,0)['x'])
    capitalCityFeature['geometry']['coordinates'].append(random_coordinates_inc(0,0)['y'])
    finalMap['features'].append(capitalCityFeature)
    # Assign a location to each of the Large Cities.
    # Draw roads from the Capital City to each of the Large Cities.
    # Assign a location to each of the Small Cities.
    # Draw roads from the closest Large City to the closest Small City.
    # Assign a location to each of the Villages.
    # Sometimes draw a road from a Village to the closest Small City.
    # Assign a location to each of the Ruins.
    # Sometimes draw a road from a Ruin to the closest Village.
    # Export the finished map.
    export_geojson(finalMap, '5thWorld.geojson')

if __name__ == "__main__":
    main(iter)
