import json
from pyls.ls import ls

def test_ls_function():
    with open("tests/structure.json", "r") as structure_file:
        mock_structure_json = json.load(structure_file)
    result = ls(mock_structure_json)

    assert result == "LICENSE README.md ast go.mod lexer main.go parser token"

def test_ls_a_function():
    with open("tests/structure.json", "r") as structure_file:
        mock_structure_json = json.load(structure_file)
    result = ls(mock_structure_json, a=True)
    assert result == ".gitignore LICENSE README.md ast go.mod lexer main.go parser token"

def test_ls_l_function():
    with open("tests/structure.json", "r") as structure_file:
        mock_structure_json = json.load(structure_file)
    result = ls(mock_structure_json, l=True)
    assert result == """drwxr-xr-x 1071 Nov 14 11:27 LICENSE
drwxr-xr-x 83 Nov 14 11:27 README.md
-rw-r--r-- 4096 Nov 14 15:58 ast
drwxr-xr-x 60 Nov 14 13:51 go.mod
drwxr-xr-x 4096 Nov 14 15:21 lexer
-rw-r--r-- 74 Nov 14 13:57 main.go
drwxr-xr-x 4096 Nov 17 12:51 parser
-rw-r--r-- 4096 Nov 14 14:57 token"""

def test_ls_r_function():
    with open("tests/structure.json", "r") as structure_file:
        mock_structure_json = json.load(structure_file)
    result = ls(mock_structure_json, r=True)
    assert result == "token parser main.go lexer go.mod ast README.md LICENSE"

def test_ls_t_function():
    with open("tests/structure.json", "r") as structure_file:
        mock_structure_json = json.load(structure_file)
    result = ls(mock_structure_json, l=True, t=True)
    assert result == """drwxr-xr-x 1071 Nov 14 11:27 LICENSE
drwxr-xr-x 83 Nov 14 11:27 README.md
drwxr-xr-x 60 Nov 14 13:51 go.mod
-rw-r--r-- 74 Nov 14 13:57 main.go
-rw-r--r-- 4096 Nov 14 14:57 token
drwxr-xr-x 4096 Nov 14 15:21 lexer
-rw-r--r-- 4096 Nov 14 15:58 ast
drwxr-xr-x 4096 Nov 17 12:51 parser"""

def test_ls_filter_function():
    with open("tests/structure.json", "r") as structure_file:
        mock_structure_json = json.load(structure_file)
    result = ls(mock_structure_json, filter="file")
    assert result == "LICENSE README.md go.mod main.go"
    result = ls(mock_structure_json, filter="dir")
    assert result == "ast lexer parser token"

def test_ls_path_function():
    with open("tests/structure.json", "r") as structure_file:
        mock_structure_json = json.load(structure_file)
    result = ls(mock_structure_json, path="parser")
    assert result == "parser_test.go parser.go go.mod"
    result = ls(mock_structure_json, path="./parser/parser.go")
    assert result == "parser.go"

def test_ls_h_function():
    with open("tests/structure.json", "r") as structure_file:
        mock_structure_json = json.load(structure_file)
    result = ls(mock_structure_json, l=True, h=True, path="parser")
    assert result == """drwxr-xr-x 1.3K Nov 17 12:51 parser_test.go
-rw-r--r-- 1.6K Nov 17 12:05 parser.go
drwxr-xr-x 533 Nov 14 16:03 go.mod"""