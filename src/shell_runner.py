import os
import json
import argparse
from utils import shell_execute_command

def run_commands(commands):
    output, error = shell_execute_command(" && ".join(commands))
    if output:
        log = f"Executed all {len(commands)} commands successfully!\n{commands}"
        print(f"STATUS: SUCCESS\nOUTPUT:{log}")
    if error:
        log = f"There was an error while executing the commands!, The Error:\n{error}"
        print(f"STATUS: ERROR\nOUTPUT:{log}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run shell commands")
    parser.add_argument(
        "--commands",
        type=json.loads,
        required=True,
        help="List of commands to execute",
    )
    args = parser.parse_args()
    commands = args.commands
    run_commands(commands)
