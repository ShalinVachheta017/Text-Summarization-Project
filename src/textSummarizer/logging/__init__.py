# Import necessary libraries for file and logging management
import os
import sys
import logging

# Define the logging format string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory and filepath for log files
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the logs directory if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Use the defined logging format
    handlers=[
        logging.FileHandler(log_filepath),  # Log to the specified file
        logging.StreamHandler(sys.stdout)  # Also log to the standard output (console)
    ]
)

# Create a logger object with a specific name
logger = logging.getLogger("textSummarizerLogger")
