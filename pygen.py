import random
import json

def random_coordinates():
    # 0 to 15, with up to 4 decimal places
    x_coord = random.uniform(0, 15)
    x_coord = round(x_coord, 4)
    y_coord = random.uniform(0, 15)
    y_coord = round(y_coord, 4)
    return {"x": x_coord, "y": y_coord}

def export_geojson(dictIn, outFile):
    json.dump(dictIn,open(outFile,"w+"), sort_keys=True, indent=4, separators=(',', ': '))

def map_setup():
    # Load in the map of Cameroon, released to Public Domain, as our base map.
    basemap = json.load(open('basemap.geojson', 'r'))
    # Replace our references to Cameroon with something more fitting.
    basemap['properties']['name'] = "5th World"
    basemap['properties']['code'] = "5WR"
    basemap['_id'] = "fifth_world"
    return basemap

def main():
    basemap = map_setup()
    # Set basemap as one of several features:
    finalMap = {}
    finalMap['type'] = 'FeatureCollection'
    finalMap['features'] = []
    finalMap['features'].append(basemap)
    # Determine the number of Large Cities we'll have, there has to be at least one.
    # Randomly choose one of the Large Cities to be the capital.
    # Determine the number of Small Cities we'll have.
    # Determine the number of Villages we'll have.
    # Determine the number of Ruins we'll have.
    # Assign a location to the Capital City.
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
    main()
