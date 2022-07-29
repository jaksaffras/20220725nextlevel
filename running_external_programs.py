import shlex
from subprocess import run, PIPE, CalledProcessError


program_to_run = "netstat -n"

cmd_words = shlex.split(program_to_run)

print(f"cmd_words: {cmd_words}")

run(cmd_words)
print('-' * 60)

try:
    process = run(cmd_words, stdout=PIPE)
except CalledProcessError as err:
    print("something went wonky")
    print("Program returned", err.returncode)
else:
    output_lines = process.stdout.decode().splitlines()
    established_connections = [line for line in output_lines if 'ESTAB' in line]

    for connection in established_connections:
        print(connection)

print()

