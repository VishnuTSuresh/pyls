def ls(structure_data):
    result_list = []
    for content in structure_data["contents"]:
        name:str = content["name"]
        if not name.startswith("."):
            result_list.append(name)
    return " ".join(result_list)