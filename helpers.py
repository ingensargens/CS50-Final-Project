import os
def setup():

    # Specify the path to your commands.txt file
    commands_file_path = "commands.txt"

    # Read and process the commands from the file
    with open(commands_file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("export "):
                key, value = line[len("export "):].split("=", 1)
                os.environ[key] = value