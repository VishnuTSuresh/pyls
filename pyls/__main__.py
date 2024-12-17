import json
import argparse

from pyls.ls import ls

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python ls implementation")
    parser.add_argument("-A", action="store_true")
    args = parser.parse_args()

    with open("structure.json") as structure_file:
        structure_data = json.load(structure_file)
        print(
            ls(
                structure_data,
                a=args.A
            )
        )