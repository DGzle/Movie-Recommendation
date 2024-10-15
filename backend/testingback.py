import os

def check_repository_cloned(repo_path, expected_files):
    """
    Check if the repository has been cloned correctly by verifying the presence of expected files.

    :param repo_path: Path to the cloned repository
    :param expected_files: List of files or directories expected to be in the repository
    :return: True if all expected files are present, False otherwise
    """
    for file in expected_files:
        if not os.path.exists(os.path.join(repo_path, file)):
            print(f"Missing expected file or directory: {file}")
            return False
    return True

if __name__ == "__main__":
    repo_path = "/c:/Users/DAGS/diego_projects/Movie-Recommendation"
    expected_files = ["README.md", "backend", "frontend"]  # Add the expected files or directories here

    if check_repository_cloned(repo_path, expected_files):
        print("Repository cloned correctly.")
    else:
        print("Repository not cloned correctly.")