# Dedicated to my sister, she gave me the idea.
import os
import openai
import requests
import json
from datetime import datetime
import argparse
import sys
# TODO: add env vaiable support for apikey
openai.api_key = ""
weatherapikey = ""
zipcode = "10001"
now = datetime.now()
def chatbot(input):
    messages = [
        {
            "role": "system",
            "content": "You are ChatGPT, a large language model trained by OpenAI.",
        },
        {"role": "system", "content": "Knowledge cutoff: 2021-09"},
        {"role": "system", "content": f"Current date and time is {now.strftime('%m/%d/%Y %H:%M')}"},
        {"role": "system", "content": f"Current weather is: {weather_data(zipcode)}"}
    ]
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content  # type: ignore
        messages.append({"role": "assistant", "content": reply})
        return reply

def weather_data(zipcode):
    response = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key={weatherapikey}&q={zipcode}&aqi=no"
    )
    jsonsinglequote = str(response.json())
    goodresponse = jsonsinglequote.replace("'", '"')
    weatherdict = json.loads(goodresponse)
    city = weatherdict["location"]["name"]
    temp = weatherdict["current"]["temp_c"]
    condition = weatherdict["current"]["condition"]["text"]
    return [city, temp, condition]
print(chatbot("hello"))
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

def metadata_add(filename, username, uid):
    with open(filename, "r") as file:
        content = file.read()

    with open(filename, "w") as file:
        file.write(f"username:{username}\nuid:{uid}\n" + content)

def getkeytowrite(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if lines:
                key = lines[-1].split(":")
                print(lines[-1])
                return int(key[0]) + 1
            else:
                raise OSError("Empty file.")
    except FileNotFoundError:
        raise FileNotFoundError("File doesn't exist.")

def write(
    filename, title, desc, datetodone, timetodone, repeat, place, priority, flagged
):
    keytowrite = getkeytowrite(filename)
    print("key is", keytowrite)
    try:
        with open(filename, "a") as file:
            value = f"{title},{desc},{datetodone},{timetodone},{repeat},{place},{priority},{flagged}"
            file.write(f"{keytowrite}:{value}\n")
    except PermissionError:
        raise PermissionError("No permission to edit file.")
    except IOError as exep:
        raise IOError(f"Unknown IO error: {exep}.")


def read(filename, key):
    title = ""
    desc = ""
    datetodone = ""
    timetodone = ""
    repeat = True
    place = ""
    priority = ""
    flagged = True
    try:
        with open(filename, "r") as file:
            data = file.readlines()
            for line in data:
                if str(line.split(":")[0]) == key:
                    rawdata = line.strip().split(":")[1]
                    (
                        title,
                        desc,
                        datetodone,
                        timetodone,
                        repeat,
                        place,
                        priority,
                        flagged,
                    ) = rawdata.split(",")
                    if repeat == "true" or "True":
                        repeat = True
                    elif repeat == "false" or "False":
                        repeat = False
                    if flagged == "true" or "True":
                        flagged = True
                    elif flagged == "false" or "False":
                        flagged = False
                    return [
                        title,
                        desc,
                        datetodone,
                        timetodone,
                        repeat,
                        place,
                        priority,
                        flagged,
                    ]

    except FileNotFoundError:
        raise FileNotFoundError("File doesn't exist.")

def delete(filename, key):
    # key NEEDS TO BE A STRING
    try:
        with open(filename, "r") as file:
            data = file.readlines()

        with open(filename, "w") as file:
            for line in data:
                if str(line.split(":")[0]) != key:
                    file.write(line)
    except FileNotFoundError:
        raise Exception(f'File named "{filename}" not found')

def edit(filename, old_key, new_value):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        with open(filename, "w") as file:
            for line in lines:
                if ":" in line:
                    key, value = line.strip().split(":")
                    key = key.strip()
                    value = value.strip()
                    if key == old_key:
                        file.write(f"{key}:{new_value}\n")
                    else:
                        file.write(line)

    except FileNotFoundError:
        raise Exception(f'File named "{filename}" not found')

