import json
import argparse
from typing import Any, Dict
from pyls.ls import ls
from pyls.help import help_statement

def main() -> None:
    """
    Main entry point for the Python `ls` implementation.
    Parses command-line arguments, loads the file structure, and executes the `ls` function.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Python ls implementation", add_help=False)
    parser.add_argument("path", nargs="?", default=".", help="Path to navigate to (default: current directory).")
    parser.add_argument("-A", action="store_true", help="Show all files except '.' and '..'.")
    parser.add_argument("-l", action="store_true", help="Use a long listing format.")
    parser.add_argument("-r", action="store_true", help="Reverse the order of the output.")
    parser.add_argument("-t", action="store_true", help="Sort by modification time.")
    parser.add_argument("-h", action="store_true", help="Display file sizes in human-readable format.")
    parser.add_argument("--help", action="store_true", help="Show help message and exit.")
    parser.add_argument("--filter", choices=["file", "dir"], help="Filter output to only files or directories.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Display the help statement if the --help flag is provided
    if args.help:
        print(help_statement)
    else:
        # Try to load the file structure from the JSON file
        try:
            with open("structure.json") as structure_file:
                structure_data: Dict[str, Any] = json.load(structure_file)
        except FileNotFoundError:
            print("Error: 'structure.json' file not found. Please ensure the file exists in the current directory.")
            return
        except json.JSONDecodeError:
            print("Error: Failed to parse 'structure.json'. Please ensure it contains valid JSON data.")
            return

        # Try to execute the `ls` function and handle potential issues
        try:
            result = ls(
                structure_data,
                show_all=args.A,
                long_format=args.l,
                reverse=args.r,
                sort_by_time=args.t,
                human_readable=args.h,
                filter_type=args.filter,
                path=args.path
            )
            print(result)
        except KeyError as e:
            print(f"Error: Invalid structure detected. Missing key: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()