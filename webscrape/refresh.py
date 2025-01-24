import time
from playwright.sync_api import sync_playwright
def refresh():
  with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=True)  # Set headless=True for no UI
    page = browser.new_page()

    # Navigate to the webpage
    url = "https://tangobot.vercel.app/api/revalidate"
    page.goto(url)

    # Wait for 5 seconds to let the page load fully
    time.sleep(5)
    browser.close()
    print("Website re-rendered")
    return True

if __name__ == "__main__":
  refresh()