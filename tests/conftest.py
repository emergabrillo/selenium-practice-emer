import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode for testing
    options.add_argument("window-size=1920,1080")  # Set window size for consistent layout

    # Built-in Selenium Manager will fetch matching driver binaries
    driver = webdriver.Chrome(options=options) 
    yield driver
    driver.quit() # Ensure the browser is closed after each test