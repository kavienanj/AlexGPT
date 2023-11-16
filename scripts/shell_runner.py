import subprocess
import json
import argparse

def run_commands(commands):
    process = subprocess.Popen(
        " && ".join(commands),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    output, error = process.communicate()
    return_code = process.wait()
    output = output.decode('utf-8').strip()
    error = error.decode('utf-8').strip()
    if output:
        print("OUTPUT:\n", output)
    if error:
        print("ERROR:\n", error)
    print("Return Code:", return_code)


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
