from prompt import SYSTEM_PROMPT
from utils.openai_models import gpt4_preview_json
import os
import json

with open("actions.json") as f:
    ACTIONS = json.load(f)

os.system("say Welcome back Sir! I am ready to help you execute your tasks")
while True:
    user_prompt = input("You: ")

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT.replace('{ACTIONS_JSON}', json.dumps(ACTIONS, indent=4)),
        },
        {
            "role": "user",
            "content": user_prompt,
        },
    ]
    response = gpt4_preview_json(messages)
    assistant_response = response["assistant_response"]
    print("AlexGPT: ", assistant_response)
    os.system(f"say '{assistant_response}'")
    if response.get("action"):
        print("Running command...")
        execute_command = response["action"]["script"]
        for parameter, value in response["action"]["parameters"].items():
            execute_command += f" --{parameter} '{json.dumps(value)}'"
        print(execute_command)
        os.system(execute_command)
        print("Command executed!")
