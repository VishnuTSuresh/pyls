# pyls: Python `ls` Implementation

`pyls` is a Python ls implementation - A utility to mimic the functionality of the Linux 'ls' command for directory structures stored in a JSON file.

## Features

- Display files and directories in a specific path.
- Show hidden files and directories (`-A`).
- Display detailed file information (`-l`).
- Sort files by modification time (`-t`).
- Reverse the output order (`-r`).
- Show file sizes in a human-readable format (`-h`).
- Filter output to only files or directories (`--filter`).
- Navigate to specific paths (`path` argument).

## Installation

### Using `pip` (with source code)
1. Clone the repository:
   ```bash
   git clone https://github.com/VishnuTSuresh/pyls.git
   cd pyls
   ```

2. Install the package:
   ```bash
   pip install .
   ```

3. Verify the installation:
   ```bash
   pyls --help
   ```

   This should display the help message for the `pyls` command.

---

## Usage

Run the `pyls` command from the terminal (Make sure that the structure.json file is in the path where pyls is being run):

```bash
pyls [options] [path]
```

### Options
- **`-A`**: Show all files except `.` and `..`.
- **`-l`**: Use a long listing format.
- **`-r`**: Reverse the order of the output.
- **`-t`**: Sort by modification time.
- **`-h`**: Display file sizes in human-readable format.
- **`--filter`**: Filter output to only files or directories (`file` or `dir`).
- **`--help`**: Show the help message and exit.

### Examples
1. List files in the current directory:
   ```bash
   pyls
   ```

2. List files in a specific directory:
   ```bash
   pyls /path/to/directory
   ```

3. Show all files, including hidden ones:
   ```bash
   pyls -A
   ```

4. Use a long listing format with human-readable sizes:
   ```bash
   pyls -l -h
   ```

5. Filter to show only files:
   ```bash
   pyls --filter file
   ```

6. Reverse the order of files:
   ```bash
   pyls -r
   ```

---

## Building the Project

If you wish to build the project from source, follow these steps:

1. Ensure you have the necessary tools installed:
   ```bash
   pip install build
   ```

2. Build the project:
   ```bash
   python -m build
   ```

3. This will generate the package files (`.whl` and `.tar.gz`) in the `dist/` directory. You can install the package locally:
   ```bash
   pip install dist/pyls-1.0.0-py3-none-any.whl
   ```

---

## Running Tests

Run the test suite using `pytest`:

```bash
python -m pytest tests/
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

[Vishnu T Suresh](mailto:vishnutsuresh@live.com)

---