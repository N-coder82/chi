#Dedicated to my sister, she gave me the idea.
weatherapikey = ""
import os
import requests
import json
#TODO: remove key param when done changing to to whats referenced in todoforbasemvp.md
def metadata_read(filename):
    key = "username"
    usernamevalue = ""
    try:
        with open(filename, "r") as file:
            data = file.readlines()
            for line in data:
                if key in line:
                    usernamevalue = line.strip().split(":")[1]
    except FileNotFoundError:
        return None
    key = "uid"
    uidvalue = ""
    try:
        with open(filename, "r") as file:
            data = file.readlines()
            for line in data:
                if key in line:
                    uidvalue = line.strip().split(":")[1]
    except FileNotFoundError:
        return None
    return [usernamevalue, uidvalue]
def metadata_add(filename,username,uid):
    with open(filename, 'r') as file:
        content = file.read()

    with open(filename, 'w') as file:
        file.write(f"username:{username}\nuid:{uid}\n" + content)
def getkeytowrite(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if lines:
                key, value = lines[-1].strip(":")
                return int(key)
            else:
                raise OSError("File selected is made of whitespace or has no data/ is empty.")
    except FileNotFoundError:
        raise FileNotFoundError("File doesn't exist.")
def weather_data(zipcode):
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={weatherapikey}&q={zipcode}&aqi=no")
    jsonsinglequote = str(response.json())
    goodresponse = jsonsinglequote.replace("'",'"')
    weatherdict = json.loads(goodresponse)
    city = weatherdict["location"]["name"]
    temp = weatherdict["current"]["temp_c"]
    condition = weatherdict["current"]["condition"]["text"]
    return [city,temp,condition]