import json
from pathlib import Path
from pyls.ls import ls

# Define the path to the test JSON file
TEST_STRUCTURE_FILE = Path("tests/structure.json")

def load_mock_structure() -> dict:
    """
    Loads the mock file system structure from the test JSON file.

    Returns:
        dict: The mock file system structure as a dictionary.
    """
    with TEST_STRUCTURE_FILE.open("r") as structure_file:
        return json.load(structure_file)

def test_ls_function():
    """
    Tests the basic functionality of the ls function.
    """
    mock_structure = load_mock_structure()
    result = ls(mock_structure)
    assert result == "LICENSE README.md ast go.mod lexer main.go parser token"

def test_ls_a_function():
    """
    Tests the ls function with the 'show_all' flag.
    """
    mock_structure = load_mock_structure()
    result = ls(mock_structure, show_all=True)
    assert result == ".gitignore LICENSE README.md ast go.mod lexer main.go parser token"

def test_ls_l_function():
    """
    Tests the ls function with the 'long_format' flag.
    """
    mock_structure = load_mock_structure()
    result = ls(mock_structure, long_format=True)
    assert result == """drwxr-xr-x 1071 Nov 14 11:27 LICENSE
drwxr-xr-x 83 Nov 14 11:27 README.md
-rw-r--r-- 4096 Nov 14 15:58 ast
drwxr-xr-x 60 Nov 14 13:51 go.mod
drwxr-xr-x 4096 Nov 14 15:21 lexer
-rw-r--r-- 74 Nov 14 13:57 main.go
drwxr-xr-x 4096 Nov 17 12:51 parser
-rw-r--r-- 4096 Nov 14 14:57 token"""

def test_ls_r_function():
    """
    Tests the ls function with the 'reverse' flag.
    """
    mock_structure = load_mock_structure()
    result = ls(mock_structure, reverse=True)
    assert result == "token parser main.go lexer go.mod ast README.md LICENSE"

def test_ls_t_function():
    """
    Tests the ls function with the 'sort_by_time' and 'long_format' flags.
    """
    mock_structure = load_mock_structure()
    result = ls(mock_structure, long_format=True, sort_by_time=True)
    assert result == """drwxr-xr-x 1071 Nov 14 11:27 LICENSE
drwxr-xr-x 83 Nov 14 11:27 README.md
drwxr-xr-x 60 Nov 14 13:51 go.mod
-rw-r--r-- 74 Nov 14 13:57 main.go
-rw-r--r-- 4096 Nov 14 14:57 token
drwxr-xr-x 4096 Nov 14 15:21 lexer
-rw-r--r-- 4096 Nov 14 15:58 ast
drwxr-xr-x 4096 Nov 17 12:51 parser"""

def test_ls_filter_function():
    """
    Tests the ls function with the 'filter_type' argument for both files and directories.
    """
    mock_structure = load_mock_structure()
    result = ls(mock_structure, filter_type="file")
    assert result == "LICENSE README.md go.mod main.go"
    result = ls(mock_structure, filter_type="dir")
    assert result == "ast lexer parser token"

def test_ls_path_function():
    """
    Tests the ls function with the 'path' argument.
    """
    mock_structure = load_mock_structure()
    result = ls(mock_structure, path="parser")
    assert result == "parser_test.go parser.go go.mod"
    result = ls(mock_structure, path="./parser/parser.go")
    assert result == "parser.go"

def test_ls_h_function():
    """
    Tests the ls function with the 'long_format', 'human_readable', and 'path' flags.
    """
    mock_structure = load_mock_structure()
    result = ls(mock_structure, long_format=True, human_readable=True, path="parser")
    assert result == """drwxr-xr-x 1.3K Nov 17 12:51 parser_test.go
-rw-r--r-- 1.6K Nov 17 12:05 parser.go
drwxr-xr-x 533 Nov 14 16:03 go.mod"""
