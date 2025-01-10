import os
import git

# Define the path to the directory where you want to clone the repository
repo_dir = "/Users/anachavez/Documents/Colaboraciones/HANA"

# Check if the directory already exists and is not empty
if os.path.exists(repo_dir) and os.listdir(repo_dir):
    # If it exists and is not empty, print a message and skip the cloning process
    print(f"Directory '{repo_dir}' already exists and is not empty. Skipping cloning.")
else:
    # If it doesn't exist or is empty, clone the repository
    git.Git().clone("https://github.com/DIFACQUIM/HANA.git", repo_dir)
    print(f"Repository cloned successfully to '{repo_dir}'.")

# Import the hana correctly
import sys
sys.path.append(repo_dir)  # Add the repository directory to the system path
from HANA.hana import hana  # Import the hana function from the correct module

# Now you can call the hana
print(hana("C1CNCCN1"))
