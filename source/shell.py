import os
import openai
import requests
import json
#TODO: add env vaiable support for apikey
openai.api_key = ""
weatherapikey = ""
def chatbot(input):
    messages = [
        {
            "role": "system",
            "content": "You are ChatGPT, a large language model trained by OpenAI.",
        },
        {"role": "system", "content": "Knowledge cutoff: 2021-09"},
    ]
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content  # type: ignore
        messages.append({"role": "assistant", "content": reply})
        return reply
def weather_data(zipcode):
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={weatherapikey}&q={zipcode}&aqi=no")
    jsonsinglequote = str(response.json())
    goodresponse = jsonsinglequote.replace("'",'"')
    weatherdict = json.loads(goodresponse)
    city = weatherdict["location"]["name"]
    temp = weatherdict["current"]["temp_c"]
    condition = weatherdict["current"]["condition"]["text"]
    return [city,temp,condition]