"""
Use conftest.py to manage the WebDriver setup and teardown
This allows reusing the driver setup across multiple test files using pytest fixtures.
"""

import pytest
from selenium import webdriver

# Define a pytest fixture to initialize and clean up the WebDriver
@pytest.fixture()
def driver():
    # Create a new instance of the Chrome WebDriver
    driver = webdriver.Chrome()

    # Maximize the browser window for better visibility during tests
    driver.maximize_window()

    # Provide the driver instance to the test function
    yield driver

    # Quit the browser after the test is done to free up resources
    driver.quit()
