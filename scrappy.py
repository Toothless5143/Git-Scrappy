from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Set the path to your chromedriver
cdp = "/home/toothless/Downloads/chromedriver"  # Change it according to your own need

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"executable_path={cdp}")

# Initialize Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Prompt the user to enter the GitHub username
username = input("Enter the GitHub username: ")

# Visit the user's GitHub profile
url = f"https://github.com/{username}"
driver.get(url)

# Wait for the page to load (optional)
time.sleep(2)

# Find all repositories
repos = driver.find_elements(By.CLASS_NAME, "repo")

# Wait for the elements to load (optional)
time.sleep(2)

# Loop through repositories
for repo in repos:
    repo_name = repo.text
    print(f"Scanning repository: {repo_name}")
    
    try:
        # Open the repository
        repo_link = repo.find_element(By.TAG_NAME, "a").get_attribute("href")
        driver.get(repo_link)
        
        # Wait for the page to load (optional)
        time.sleep(2)
        
        # Find all files in the repository
        files = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
        
        # Loop through files
        for file in files:
            file_name = file.text
            file_link = file.get_attribute("href")
            driver.get(file_link)
            
            # Wait for the page to load (optional)
            time.sleep(2)
            
            # Get the file content
            file_content = driver.find_element(By.CLASS_NAME, "highlight").text
            
            # Check if "funny" is present in the file content
            if "password" in file_content:
                print(f"Found 'password' in file: {file_name}")
                lines = file_content.split("\n")
                
                # Print lines containing "funny"
                for line in lines:
                    if "funny" in line:
                        print(line)
    
    except NoSuchElementException:
        print("No repositories found.")
    
# Quit the driver
driver.quit()
