import json
from create_db import AddEntry, CreateDataBase, QueryCurs
import csv

with open('peugeotsmall.geojson') as json_data:
    dict_from_peugeot = json.load(json_data)
    json_data.close()

for key in dict_from_peugeot['features']:
    city = key['properties']["nomb"]
    longitude = key['geometry']['coordinates'][0]
    latitude = key['geometry']['coordinates'][1]

    AddEntry(city, longitude, latitude)

CreateDataBase.commit()

QueryCurs.execute('SELECT * FROM Peugeots')

for value in QueryCurs:
    with open('peugeot.csv', 'a', newline='') as f:
        ecrire = csv.writer(f)
        ecrire.writerow([value[1], value[2], value[3]])

QueryCurs.close()

coordinates = []
with open('peugeot.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        coordinates.append([float(row[1]), float(row[2])])

geojson = {"type": "MultiPoint",
           "coordinates": coordinates
           }


def generate_geojson():
    with open('peugeot.geosjon', 'w') as my_data_file:
        json.dump(geojson, my_data_file)


generate_geojson()
