from prompt import SYSTEM_PROMPT
import os
import json
from src.openai_models import gpt4o_json
from src.utils import shell_execute_command

with open("actions.json") as f:
    ACTIONS = json.load(f)

ALEX_GPT_MESSAGES = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT.replace('{ACTIONS_JSON}', json.dumps(ACTIONS, indent=4)),
    },
]

os.system("say \"Welcome back Sir! I am ready to help you execute your tasks\"")
while True:
    user_prompt = input("You: ")
    ALEX_GPT_MESSAGES.append({
        "role": "user",
        "content": user_prompt,
    })
    response = gpt4o_json(ALEX_GPT_MESSAGES)
    assistant_response = response["assistant_response"]
    print("AlexGPT: ", assistant_response)
    os.system(f"say \"{assistant_response}\"")
    if response.get("action"):
        print("Running command...")
        execute_command = response["action"]["script"]
        for parameter, value in response["action"]["parameters"].items():
            if str(value).isnumeric():
                execute_command += f" --{parameter} {int(value)}"
            else:
                execute_command += f" --{parameter} '{json.dumps(value)}'"
        print(execute_command)
        output, error = shell_execute_command(execute_command)
        if output:
            print("AlexGPT: ", output)
            os.system(f"say \"{output}\"")
            assistant_response += f"\nEXECUTION MESSAGE:\n{output}"
        elif error:
            print("AlexGPT: ", error)
            os.system(f"say \"{error}\"")
            assistant_response += f"\nEXECUTION MESSAGE:\n{error}"
    ALEX_GPT_MESSAGES.append({
        "role": "assistant",
        "content": assistant_response,
    })
