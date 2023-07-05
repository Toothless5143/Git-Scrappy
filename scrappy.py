from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the path to your chromedriver
cdp = "#" # Change it according to your own need
driver = webdriver.Chrome(executable_path=cdp)

# Prompt the user to enter the username
username = input("Enter the GitHub username: ")

url = f"https://github.com/{username}"
driver.get(url)
repo = f"https://github.com/{username}"

# Wait for the page to load (optional)
# time.sleep(2)

# Find all elements
res = driver.find_elements(By.CLASS_NAME, "repo")

# Wait for the elements to load (optional)
# time.sleep(2)

links = []
flink = []

def get_raw(second_page):
    driver.get(second_page)
    raw = driver.find_element(By.CLASS_NAME, "js-permalink-replaceable-link")
    raw.click()
    html = driver.page_source
    html = f"{html}"
    if "password" in html:
        print(f"Found password on {second_page}")

def loop(next_page):
    global a
