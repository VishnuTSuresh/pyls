from datetime import datetime
from pathlib import Path
from typing import Dict, Union

def format_time(epoch_time: int) -> str:
    """
    Converts epoch time to a formatted string.

    Args:
        epoch_time (int): The epoch time to convert.

    Returns:
        str: A formatted string representing the time.
    """
    return datetime.fromtimestamp(epoch_time).strftime('%b %d %H:%M')

def navigate_to_path(node: Dict[str, Union[str, list]], path: str) -> Dict[str, Union[str, list]]:
    """
    Navigates to the specified path within the directory structure.

    Args:
        node (Dict[str, Union[str, list]]): The root of the directory structure.
        path (str): The path to navigate to.

    Returns:
        Dict[str, Union[str, list]]: The node corresponding to the final directory or file.
    """
    path_components = [part for part in Path(path).parts if part not in ('.', '')]
    for part in path_components:
        node = next((item for item in node["contents"] if item["name"] == part), None)
    return node

def human_readable_size(size: int) -> str:
    """
    Converts a size in bytes to a human-readable format.

    Args:
        size (int): The size in bytes.

    Returns:
        str: The size in a human-readable format (e.g., KB, MB, GB).
    """
    for unit in ['B', 'K', 'M', 'G']:
        if size < 1024:
            if unit == "B":
                return f"{size}"
            else:
                return f"{size:.1f}{unit}"
        size /= 1024
