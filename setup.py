# Import the setuptools library which provides tools for packaging Python projects
import setuptools

# Open and read the contents of the README.md file for the long description of the package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the version of the package
__version__ = "0.0.0"

# Define metadata for the package
REPO_NAME = "Text-Summarization-Project"  # The name of the GitHub repository
AUTHOR_USER_NAME = "ShalinVachheta017"  # GitHub username of the author
SRC_REPO = "textSummarizer"  # The name of the source repository
AUTHOR_EMAIL = "shalinvachheta2016@hotmail.com"  # Author's email address

# Setup function to provide package details and metadata
setuptools.setup(
    name=SRC_REPO,  # Name of the package
    version=__version__,  # Version of the package
    author=AUTHOR_USER_NAME,  # Author's GitHub username
    author_email=AUTHOR_EMAIL,  # Author's email address
    # Short description of the package
    description="A small python package for NLP app",
    long_description=long_description,  # Long description read from README.md
    # The format of the long description
    long_description_content_type="text/markdown",
    # URL of the project repository
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        # URL for the bug tracker
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Directory where the packages are located
    # Automatically find packages in the specified directory
    packages=setuptools.find_packages(where="src")
)
