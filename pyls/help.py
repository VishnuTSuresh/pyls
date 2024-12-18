help_statement = """
Python ls implementation - A utility to mimic the functionality of the Linux 'ls' command for directory structures stored in a JSON file.

Usage:
  python -m pyls [OPTIONS] [PATH]

Options:
  -A                   Include entries starting with '.' (hidden files).
  -l                   List details such as permissions, size, modification time, and name.
  -r                   Reverse the order of the output.
  -t                   Sort by modification time, newest first.
  -h                   Show human-readable file sizes (e.g., 1K, 2M).
  --filter {file,dir}  Filter output to show only 'file' or 'dir'.
  --help               Show this help message and exit.

Arguments:
  PATH                 Path to the directory or file. Defaults to the current directory.
"""