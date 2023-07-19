import time
import json
import random

aList = []

start_time = time.time()
time_multiplier = 60

#76.9330689, 43.2362883, 810355

const_longitude = 76.9330689
const_latitude = 43.2362883
const_altitude = 830.355

longitude = const_longitude
latitude = const_latitude
altitude = const_altitude

distance = 0.0000300
max_length = 0.0001000
width = 0.0003000

for i in range(5):
    for j in range(15):
        temp_dict = {}

        temp_dict["time"] = time.ctime(start_time + (j * time_multiplier))
        temp_dict["coordinates"] = {
            "longitude": longitude,
            "latitude": latitude,
            "altitude": altitude
        }
        temp_dict["data"] = {
            "NO2": random.randint(0, 2000),
            "CO": random.randint(0, 500),
            "SO2": random.randint(0, 500),
            "O3": random.randint(0, 500),
            "PM": random.randint(0, 500),
            "Humidity": random.randint(40, 60),
            "Temperature": random.randint(22, 26)
        }

        longitude = round(const_longitude + random.uniform(-0.0000300, 0.0000300), 7)
        latitude = round(latitude + distance + random.uniform(-0.0000010, 0.0000010), 7)
        altitude = round(const_altitude + random.uniform(-1, 1), 3)

        aList.append(temp_dict)
    
    distance *= -1

    const_longitude = round(const_longitude + width, 7)

print(aList)

json_data = json.dumps(aList)

jsonFile = open("generated_data.json", "w")
jsonFile.write(json_data)
jsonFile.close()