import time
from playwright.sync_api import sync_playwright

# Start Playwright
with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False)  # Set headless=True for no UI
    page = browser.new_page()

    # Navigate to the webpage
    url = "https://www.linkedin.com/games/view/tango/desktop"
    page.goto(url)

    # Wait for 5 seconds to let the page load fully
    time.sleep(5)

    # Get the generated HTML after JavaScript execution
    generated_html = page.content()

    # Split the HTML content into an array of lines
    html_array = generated_html.splitlines()

    # Print the first 5 lines
    for line in html_array:
        print(line)

    # Close the browser
    browser.close()