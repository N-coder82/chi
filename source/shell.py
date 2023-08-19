import os
import openai
#TODO: add env vaiable support for apikey
openai.api_key = ""
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
