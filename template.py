# Import necessary libraries for file and directory management
import os
from pathlib import Path
import logging

# Set up logging configuration to display info messages with timestamps
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = "textSummarizer"

# List of files and directories to be created for the project
list_of_files = [
    ".github/workflows/.gitkeep/",  # Directory to keep CI/CD workflow files
    # Initializer for the main project package
    f"src/{project_name}/__init__.py",
    # Initializer for the components module
    f"src/{project_name}/components/__init__.py",
    # Initializer for the utils module
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",  # Common utility functions
    # Initializer for the logging module
    f"src/{project_name}/logging/__init__.py",
    # Initializer for the config module
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",  # Configuration settings
    # Initializer for the pipeline module
    f"src/{project_name}/pipeline/__init__.py",
    # Initializer for the entity module
    f"src/{project_name}/entity/__init__.py",
    # Initializer for the constants module
    f"src/{project_name}/constan/__init__.py",
    "config/config.yaml",  # Configuration file in YAML format
    "params.yaml",  # Parameters file in YAML format
    "app.py",  # Main application script
    "main.py",  # Main entry point script
    "Dockerfile",  # Docker configuration file
    "requirements.txt",  # List of dependencies
    "setup.py",  # Setup script for packaging the project
    "research/traials.ipynb",  # Jupyter notebook for research and trials
    "test.py"  # Test script
]

# Iterate through the list of files to create them if they do not exist
for filepath in list_of_files:
    # Convert the file path to a Path object
    filepath = Path(filepath)
    # Separate the directory and file name from the path
    filedir, filename = os.path.split(filepath)

    # Create the directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir} for the file {filename}")

    # Create an empty file if it does not exist or if it is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Create an empty file
            logging.info(f"Creating empty file: {filepath}")
    else:
        # Log a message if the file already exists
        logging.info(f"File {filepath} already exists")
