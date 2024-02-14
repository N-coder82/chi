# Dedicated to my sister, she gave me the idea.
import os
from openai import OpenAI
import requests
import json
from datetime import datetime
client = OpenAI()
weatherapikey = os.environ['WEATHER_API_KEY']
now = datetime.now()

zipcode = "10001"


def chatbot(input,remindersinput):
    messages = [
        {"role": "system","content": "You are Chi, a large language model trained by OpenAI and currently used by JSdev",},
        {"role": "system", "content": "Knowledge cutoff: 2021-09"},
        {"role": "system","content": f"Current date and time is {now.strftime('%m/%d/%Y %H:%M')}",},
        {"role": "system", "content": f"Current weather is: {weather_data(zipcode)}"},
        {"role": "system", "content": f"These are the users reminders: {remindersinput}\n they can acess them however they like and you will answer any questions they have about them."},
    ]
    if input:
        messages.append({"role": "user", "content": input})
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
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

def getkeytowrite(filename):
    print("hello from getkeytowrite()!")
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if lines:
                key = lines[-1].split(":")
                # print(lines[-1])
                return int(key[0]) + 1
            else:
                return 1
    except FileNotFoundError:
        raise FileNotFoundError("File doesn't exist.")

def write(
    filename,
    title,
    desc,
    datetodone,
    timetodone,
    repeatbool,
    repeat_day,
    repeat_year,
    place,
    priority,
    flagged,
):
    print("about to call getkeytowrite()")
    keytowrite = getkeytowrite(filename)
    print("got key to write")
    try:
        print("about to write")
        with open(filename, "a") as file:
            value = f"{title},{desc},{datetodone},{timetodone},{repeatbool},{repeat_day},{repeat_year},{place},{priority},{flagged}"
            file.write(f"{keytowrite}:{value}\n")
        print("written")
    except PermissionError:
        raise PermissionError("No permission to edit file.")
    except IOError as exep:
        raise IOError(f"Unknown IO error: {exep}.")

# write("reminders.chi","beep2", "borp","1/1/00","12.00 AM","False","1","2", "idk","4 - Highest","False")
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
                        repeatbool,
                        repeat_day,
                        repeat_year,
                        place,
                        priority,
                        flagged,
                    ) = rawdata.split(",")
                    h, m = timetodone.split(".")
                    timetodone = h + ":" + m
                    return {
                        "Title": title,
                        "Desc": desc,
                        "Date": datetodone,
                        "Time": timetodone,
                        "Repeating": repeatbool,
                        "Repeating / Year": repeat_year,
                        "Repeating / Day": repeat_day,
                        "Place": place,
                        "Priority": priority,
                        "Flagged": flagged,
                    }

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
