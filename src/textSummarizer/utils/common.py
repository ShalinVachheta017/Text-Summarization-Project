 # Import necessary libraries
import os
from box.exceptions import BoxValueError  # Exception handling for Box
import yaml  # YAML file handling
from textSummarizer.logging import logger  # Custom logger
from ensure import ensure_annotations  # Ensure annotations for type checking
from box import ConfigBox  # Box for dictionary access with dot notation
from pathlib import Path  # Path handling
from typing import Any  # Type hinting

# Function to read a YAML file and return its content as a ConfigBox object
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content.

    Args:
        path_to_yaml (Path): Path to the YAML file

    Raises:
        ValueError: If the YAML file is empty
        e: Any other exception

    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  # Load YAML content
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)  # Return as ConfigBox
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e

# Function to create directories from a list of paths
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories.

    Args:
        path_to_directories (list): List of directory paths to create
        verbose (bool, optional): If True, logs the creation of each directory. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Create directory
        if verbose:
            logger.info(f"Created directory at: {path}")

# Function to get the size of a file in KB
@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB.

    Args:
        path (Path): Path to the file

    Returns:
        str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Calculate size in KB
    return f"~ {size_in_kb} KB"
