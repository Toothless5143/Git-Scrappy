import requests
import re

def scan_repositories(username):
    # Make a request to the GitHub API to fetch the user's repositories
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch repositories for user {username}.")
        return

    repositories = response.json()

    # Iterate over each repository
    for repo in repositories:
        try:
            repo_name = repo["name"]
            print(f"Scanning repository: {repo_name}")

            # Make a request to fetch the contents of the repository
            contents_url = f"https://api.github.com/repos/{username}/{repo_name}/contents"
            contents_response = requests.get(contents_url)
            contents = contents_response.json()

            # Iterate over each file in the repository
            for item in contents:
                if item["type"] == "file":
                    file_url = item["download_url"]

                    # Make a request to fetch the file contents
                    file_response = requests.get(file_url)
                    file_contents = file_response.text

                    # Check if the file contains any usernames or passwords using regex pattern
                    pattern = r"(?i)\b(?:user(?:name)?|pass(?:word)?)\b:\s*(\S+)"
                    matches = re.findall(pattern, file_contents)

                    # Print the matches
                    for match in matches:
                        print(f"In file: {item['name']}")
                        print(f"Match: {match}")
                        print("-" * 50)

        except KeyError:
            print("Error accessing repository information.")
            continue

# Ask for GitHub username input
username = input("Enter a GitHub username: ")
scan_repositories(username)
