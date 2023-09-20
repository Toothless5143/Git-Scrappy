# GitHub Repository Scanner

The GitHub Repository Scanner is a command-line tool designed to scan a user's GitHub repositories for files containing potential usernames and passwords. It utilizes the GitHub API, regular expressions, and the `requests` module to fetch repository and file information, search for specified patterns, and provide detailed results.

### Features:

- Fetches repositories of a specified GitHub user.
- Retrieves the contents of each repository.
- Searches for files within the repositories.
- Scans file contents for potential usernames and passwords.
- Prints detailed information about the files and matched patterns.

### Installation:

To use the GitHub Repository Scanner, follow these installation steps:

1. Ensure that Python 3 is installed on your system.
2. Download the repository by running the following command:
   ```
   git clone https://github.com/Toothless5143/Git-Scrappy.git && cd Git-Scrappy
   ```
3. Install the required modules by running the following command:

   ```
   pip install requests
   ```

   This command installs the `requests` module, which is used for making HTTP requests.

4. The `re` module is a built-in Python module, so no additional installation is needed.

### Usage:

To run the GitHub Repository Scanner, follow these steps:

1. Open a command-line interface.
2. Navigate to the directory where the script is located.
3. Run the following command:

   ```
   python scanny.py
   ```

4. Enter the GitHub username you want to scan when prompted.
5. The tool will start scanning the user's repositories, displaying progress and any matches found.
6. Review the results, which include the file names, line numbers, and matched patterns.

### License
This tool is open source and available under the [MIT License.](/LICENSE)
