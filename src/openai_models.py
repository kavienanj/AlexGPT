import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)

def gpt4o_json(messages):
    completion = client.chat.completions.create(
        model="gpt-4o",
        response_format={ "type": "json_object" },
        messages=messages,
        temperature=1,
    )
    return json.loads(completion.choices[0].message.content)


def gpt4_preview_json(messages) -> dict:
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={ "type": "json_object" },
        messages=messages,
        temperature=1,
    )
    return json.loads(completion.choices[0].message.content)
