import json
import argparse

from pyls.ls import ls
from pyls.help import help_statement

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python ls implementation", add_help=False)
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("-A", action="store_true")
    parser.add_argument("-l", action="store_true")
    parser.add_argument("-r", action="store_true")
    parser.add_argument("-t", action="store_true")
    parser.add_argument("-h", action="store_true")
    parser.add_argument("--help", action="store_true")
    parser.add_argument("--filter", choices=["file", "dir"])
    args = parser.parse_args()
    if args.help:
        print(help_statement)
    else:
        with open("structure.json") as structure_file:
            structure_data = json.load(structure_file)
            print(
                ls(
                    structure_data,
                    a=args.A,
                    l=args.l,
                    r=args.r,
                    t=args.t,
                    h=args.h,
                    filter=args.filter,
                    path=args.path
                )
            )