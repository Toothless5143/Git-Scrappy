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
   git clone https://github.com/Toothless5143/Git-Scrapy.git && cd Git-Scrapy
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
   python scrapy.py
   ```

4. Enter the GitHub username you want to scan when prompted.
5. The tool will start scanning the user's repositories, displaying progress and any matches found.
6. Review the results, which include the file names, line numbers, and matched patterns.

### Usage in Information Disclosure:

The GitHub Repository Scanner can be a valuable tool in identifying sensitive information disclosure during security assessments, enumeration, or bug bounty hunting. Here's how it can be utilized:

- Information Disclosure: By scanning GitHub repositories, the tool helps identify potential instances of sensitive information, such as usernames and passwords, being inadvertently exposed in source code or configuration files. This can assist security professionals in identifying and mitigating information disclosure risks before they are exploited.

- Enumeration: During enumeration, the scanner can be used to gather intelligence about an organization or individual by searching for sensitive information in public GitHub repositories. It can help identify potential weak points, misconfigurations, or developmental artifacts that may reveal sensitive data, allowing for targeted testing and assessment.

- Bug Bounty Hunting: The GitHub Repository Scanner can be a valuable asset for bug bounty hunters. It can aid in the discovery of vulnerabilities by identifying instances where sensitive information, such as credentials, may have been inadvertently exposed. By proactively identifying such issues, bug bounty hunters can report them to the relevant organizations, potentially earning rewards and contributing to improved security.


### License
This tool is open source and available under the [MIT License.](/LICENSE)
