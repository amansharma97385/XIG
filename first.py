import os
import subprocess
from datetime import datetime

# Set your repository path
repo_path = "C:\Users\amans\OneDrive\Desktop\Evil_git"  

# The file to modify or create for committing
file_to_commit = "commit_streak.txt"

# Git user details (You can skip this if set globally)
git_user_name = "amansharma97385"
git_user_email = "amansharma97385@gmail.com"

# Change to the repository directory
os.chdir(repo_path)

# Set git user config if not set globally (optional)
subprocess.run(["git", "config", "user.name", git_user_name])
subprocess.run(["git", "config", "user.email", git_user_email])

# Check the file's existence, create if it doesn't exist
if not os.path.exists(file_to_commit):
    with open(file_to_commit, 'w') as f:
        f.write("GitHub contribution automation started.")

# Modify the file (this is just for the sake of making a commit)
with open(file_to_commit, 'a') as f:
    f.write(f"\nCommit made on {datetime.now()}")

# Stage the changes
subprocess.run(["git", "add", file_to_commit])

# Commit the changes
subprocess.run(["git", "commit", "-m", f"Automated commit: {datetime.now()}"])

# Push to GitHub (Assumes your remote is named 'origin' and you're pushing to the 'main' branch)
subprocess.run(["git", "push", "origin", "main"])  # or 'master' if your repo uses master
