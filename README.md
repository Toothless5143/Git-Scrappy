# Git-Scrappy
This tool is written in python to scrape passwords from a provided github username. You can use this tool for bug hunting or during pentesting. This tool will simply visit the provided github user profile and scan all the repositories for credentials.

### Installation
First you need to install the library using pip, we're using a specific version here.<br>
`pip install selenium`

Then you need to have chrome installed on your machine and you need to download the [chrome driver](https://chromedriver.chromium.org/downloads), and change the cdp variable to the path of the driver in the src code.

Then you need to run the code and provide the username.<br>
`python3 scrappy.py`

### License
This tool is open source and available under the [MIT License.](/LICENSE)
