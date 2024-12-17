import json
from pyls.ls import ls

if __name__ == "__main__":
    with open("structure.json") as structure_file:
        structure_data = json.load(structure_file)
        print(ls(structure_data))