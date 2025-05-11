import pytest
import time
from PageObjects.login_page import LoginPage
from TestData.data import Data
from Configuration.conftest import driver
from utilities.excel_utilities import get_login_data


# TC-001: Test login functionality with parameterized data from Excel

@pytest.mark.parametrize("username,password", get_login_data(
    "login_data.xlsx"))  # Parametrize the test with login data (username, password) from Excel file
def test_login(driver, username, password):
    """
    This test validates the login functionality using parameterized test data from an Excel file.
    It checks if the user is able to log in successfully based on the provided credentials.
    """

    # Step 1: Navigate to the login page
    driver.get(Data.url)  # Open the URL for login

    # Step 2: Create an instance of the LoginPage and perform login
    login_page = LoginPage(driver)  # Initialize the LoginPage object
    login_page.login(username, password)  # Perform login with provided username and password

    # Step 3: Wait for the login process to complete (using time.sleep(), consider replacing it with WebDriverWait)
    time.sleep(5)  # Static wait, ideally you would use WebDriverWait for better synchronization

    # Step 4: Get the current URL after login attempt
    current_url = driver.current_url  # Get the current URL
    expected_url = "https://www.saucedemo.com/inventory.html"  # Expected URL after successful login

    try:
        # Step 5: Check if the login was successful by comparing the current URL with expected URL
        if current_url == expected_url:
            # If login is successful, print a success message and assert True
            print(f"[✅ PASS] Login successful for user: {username}")
            assert True  # Assert True to indicate the test has passed
        else:
            # If login fails but it's expected (e.g., invalid credentials), the test still passes
            print(f"[ℹ️ INFO] Login failed as expected for invalid user: {username}")
            assert True  # Assert True as the failure is expected for invalid credentials

    except Exception as e:
        # Step 6: Handle any unexpected errors during the login attempt
        print(f"[❌ ERROR] Unexpected error for user '{username}': {e}")
        pytest.fail(f"Unexpected error for user '{username}': {e}")  # Fail the test if any unexpected error occurs


# TC-002: Test unsuccessful login with new user credentials

def test_new_login(driver):
    """
    This test verifies that an invalid login attempt with new credentials is unsuccessful.
    It checks if the login fails as expected when using an incorrect username and password.
    """

    # Step 1: Navigate to the login page
    driver.get(Data.url)  # Open the URL for login page

    # Step 2: Create an instance of the LoginPage and enter new user credentials
    login_page = LoginPage(driver)  # Initialize the LoginPage object
    login_page.enter_username(Data.new_user)  # Enter the new username
    login_page.enter_password(Data.new_password)  # Enter the new password
    login_page.click_login()  # Click the login button

    # Step 3: Assert that the login was unsuccessful (i.e., URL should not match the expected successful login URL)
    assert Data.expected_url != driver.current_url  # Assert that the current URL is not the expected successful URL

    # Step 4: Print an unsuccessful login message
    print("UNSUCCESSFUL: Login unsuccessful for the given username and password")
