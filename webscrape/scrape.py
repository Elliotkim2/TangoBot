import time
from playwright.sync_api import sync_playwright

# Start Playwright
def scrape():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=True)  # Set headless=True for no UI
        page = browser.new_page()

        # Navigate to the webpage
        url = "https://www.linkedin.com/games/view/tango/desktop"
        page.goto(url)

        # Wait for 2 seconds to let the page load fully
        time.sleep(2)

        # Get the generated HTML after JavaScript execution
        generated_html = page.content()

        # Split the HTML content into an array of lines
        html_array = generated_html.splitlines()

        # Print the lines
        # for line in html_array:
        #     print(line)

        # Close the browser
        browser.close()
        return html_array
    return []

if __name__ == "__main__":
    pass