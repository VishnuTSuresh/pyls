from datetime import datetime
from pathlib import Path

def ls(structure_data, a=False, l=False, r=False, t=False, h=False, filter=None, path="."):
    structure_data = navigate_to_path(structure_data, path)
    contents = structure_data["contents"].copy() if "contents" in structure_data else [structure_data.copy()]
    if filter is not None:
        if filter == "dir":
            contents = [content for content in contents if "contents" in content]
        if filter == "file":
            contents = [content for content in contents if "contents" not in content]
    if t:
        contents = sorted(contents, key=lambda content: content["time_modified"])
    if r:
        contents = reversed(contents)
    if not a:
        contents = [content for content in contents if not content["name"].startswith(".")]

    if not l:
        file_names:list[str] = [content["name"] for content in contents]
        result = " ".join(file_names)
    else:
        rows = [
            f"{content['permissions']} {human_readable_size(content["size"]) if h else content["size"]} {format_time(content['time_modified'])} {content["name"]}"
            for content in contents
        ]
        result = "\n".join(rows)

    return result

def format_time(epoch_time):
    return datetime.fromtimestamp(epoch_time).strftime('%b %d %H:%M')

def navigate_to_path(node, path):
    path_components = [part for part in Path(path).parts if part not in ('.', '')]
    for part in path_components:
        node = next((item for item in node["contents"] if item["name"] == part), None)
    return node

def human_readable_size(size):
    for unit in ['B', 'K', 'M', 'G']:
        if size < 1024:
            if unit == "B":
                return f"{size}"
            else:
                return f"{size:.1f}{unit}"
        size /= 1024