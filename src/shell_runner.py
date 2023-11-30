import os
import json
import argparse
from utils import shell_execute_command

def run_commands(commands, show_output=False):
    output, error = shell_execute_command(" && ".join(commands))
    if output:
        log = f"Executed all {len(commands)} commands successfully!\n{commands}"
        print(f"STATUS: SUCCESS\nLOG:{log}")
        if show_output:
            print(f"OUTPUT:\n{output}")
    if error:
        log = f"There was an error while executing the commands!, The Error:\n{error}"
        print(f"STATUS: ERROR\LOG:{log}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run shell commands")
    parser.add_argument(
        "--commands",
        type=json.loads,
        required=True,
        help="List of commands to execute",
    )
    parser.add_argument(
        "--show-output",
        type=bool,
        default=False,
        help="Show output of the commands",
    )
    args = parser.parse_args()
    commands = args.commands
    show_output = args.show_output
    run_commands(commands, show_output)
