import os

def check_file_exists(file_path):
    if os.path.isfile(file_path):
        print(f"File '{file_path}' exists. Git clone was successful.")
    else:
        print(f"File '{file_path}' does not exist. Git clone might have failed.")

# Replace 'README.md' with a file you expect to be in the cloned repository
check_file_exists('README.md')