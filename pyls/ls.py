def ls(structure_data, a=False):
    file_names:list[str] = [content["name"] for content in structure_data["contents"]]
    if a == False:
        file_names = [file_name for file_name in file_names if not file_name.startswith(".")]
    
    return " ".join(file_names)