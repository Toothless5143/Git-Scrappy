from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Prompt the user to enter the username
    username = input("Enter the GitHub username: ")

    url = f"https://github.com/{username}"
    page.goto(url)

    # Wait for the page to load (optional)
    # page.wait_for_load_state('networkidle')

    # Find all elements with class name "repo"
    repos = page.query_selector_all('.repo')

    # Wait for the elements to load (optional)
    # page.wait_for_load_state('networkidle')

    links = []

    def get_raw(second_page):
        page.goto(second_page)
        raw = page.query_selector('.js-permalink-replaceable-link')
        raw.click()
        html = page.content()
        html = f"{html}"
        if "password" in html:
            print(f"Found password on {second_page}")

    def loop(next_page):
        global links
        # Do something with the next page
        links.append(next_page)

    # Call the functions or perform the desired actions here

    browser.close()
