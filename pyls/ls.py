from pyls.utils import navigate_to_path, format_time, human_readable_size
from typing import Dict, List, Optional, Union

def ls(
    structure_data: Dict[str, Union[str, int, List[Dict]]],
    show_all: bool = False,
    long_format: bool = False,
    reverse: bool = False,
    sort_by_time: bool = False,
    human_readable: bool = False,
    filter_type: Optional[str] = None,
    path: str = "."
) -> str:
    """
    Lists the contents of a directory structure based on specified options.

    Args:
        structure_data (Dict[str, Union[str, int, List[Dict]]]): The data structure representing the file system.
        show_all (bool): Whether to show hidden files (default: False).
        long_format (bool): Whether to display detailed file information (default: False).
        reverse (bool): Whether to reverse the order of the output (default: False).
        sort_by_time (bool): Whether to sort the contents by modification time (default: False).
        human_readable (bool): Whether to display file sizes in human-readable format (default: False).
        filter_type (Optional[str]): Filter to apply ("dir" for directories, "file" for files) (default: None).
        path (str): Path to navigate to within the file system structure (default: ".").

    Returns:
        str: A formatted string of the directory contents.
    """
    # Navigate to the specified path within the directory structure
    structure_data = navigate_to_path(structure_data, path)

    # Retrieve the contents of the directory or handle the case where it's a file
    contents: List[Dict] = structure_data["contents"].copy() if "contents" in structure_data else [structure_data.copy()]

    # Apply the specified filter (if any) to include only directories or files
    if filter_type is not None:
        if filter_type == "dir":
            # Include only directories
            contents = [content for content in contents if "contents" in content]
        if filter_type == "file":
            # Include only files
            contents = [content for content in contents if "contents" not in content]

    # Sort the contents by modification time if the sort_by_time flag is enabled
    if sort_by_time:
        contents = sorted(contents, key=lambda content: content["time_modified"])

    # Reverse the order of the contents if the reverse flag is enabled
    if reverse:
        contents = list(reversed(contents))

    # Exclude hidden files (those starting with ".") unless the show_all flag is enabled
    if not show_all:
        contents = [content for content in contents if not content["name"].startswith(".")]

    # Format the output
    if not long_format:
        # If long format is not enabled, only display the names of the files/directories
        file_names: List[str] = [content["name"] for content in contents]
        result = " ".join(file_names)
    else:
        # If long format is enabled, include detailed information for each entry
        rows: List[str] = []
        for content in contents:
            # Convert the file size to a human-readable format if the flag is enabled
            size = human_readable_size(content["size"]) if human_readable else str(content["size"])
            # Format the modification time
            time = format_time(content["time_modified"])
            # Create a formatted string for each entry
            rows.append(f"{content['permissions']} {size} {time} {content['name']}")
        # Join the rows into the final output
        result = "\n".join(rows)

    # Return the formatted result
    return result
