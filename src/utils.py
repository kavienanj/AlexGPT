import subprocess

def shell_execute_command(command):
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    output, error = process.communicate()
    process.wait()
    output = output.decode('utf-8').strip()
    error = error.decode('utf-8').strip()
    return output, error
