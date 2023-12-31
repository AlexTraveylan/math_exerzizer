"""
File read adapter
author: Alex Traveylan
date: 2021-03-07
"""
from app.core.app_types import PathLike


def read_file(file_path: PathLike) -> list[str]:
    """
    Read a file and return its content as a list of lines

    Parameters
    ----------
    file_path : PathLike
        path to the file to read
    """

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    return lines


def save_file(file_path: PathLike, content: str) -> None:
    """
    Save a file with the given content

    Parameters
    ----------
    file_path : PathLike
        path to the file to save
    content : str
        content to save in the file
    """

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
