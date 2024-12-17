from datetime import datetime


def ls(structure_data, a=False, l=False):
    contents = structure_data["contents"].copy()

    if not a:
        contents = [content for content in contents if not content["name"].startswith(".")]

    if not l:
        file_names:list[str] = [content["name"] for content in contents]
        result = " ".join(file_names)
    else:
        rows = [f"{content['permissions']} {content["size"]} {datetime.fromtimestamp(content['time_modified']).strftime('%b %d %H:%M')} {content["name"]}" for content in contents]
        result = "\n".join(rows)
    
    return result