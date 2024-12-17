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