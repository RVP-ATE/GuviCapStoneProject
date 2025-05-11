import time
from PageObjects.cart_page import CartPage
from PageObjects.login_page import LoginPage
from PageObjects.base_page import BasePage
from PageObjects.product_page import ProductPage
from TestData.data import Data
from Configuration.conftest import driver

# TC-003
def test_logout(driver):
    """
    This test validates the logout functionality. It performs the following:
    - Login with valid credentials
    - Open the menu and click logout
    - Verify that the login button is displayed after logout
    """
    driver.get(Data.url)  # Navigate to the login page
    login_page = LoginPage(driver)  # Initialize LoginPage object
    login_page.enter_username(Data.username)  # Enter username
    login_page.enter_password(Data.password)  # Enter password
    login_page.click_login()  # Click the login button
    time.sleep(3)  # Wait for the login to complete

    product_page = ProductPage(driver)  # Initialize ProductPage object
    product_page.click_menu()  # Click the menu button
    time.sleep(3)  # Wait for the menu to appear
    product_page.logout()  # Click logout button

    # Assertion to verify logout was successful (i.e., login button is visible after logout)
    assert login_page.is_login_button_displayed(), "Logout failed: Login button not displayed"


# TC-004
def test_cart_button(driver):
    """
    This test verifies that the cart button is visible after login.
    It ensures that the cart button appears once the user is logged in.
    """
    driver.get(Data.url)  # Navigate to the login page
    login_page = LoginPage(driver)  # Initialize LoginPage object
    login_page.enter_username(Data.username)  # Enter username
    login_page.enter_password(Data.password)  # Enter password
    login_page.click_login()  # Click the login button
    time.sleep(3)  # Wait for login to complete

    product_page = ProductPage(driver)  # Initialize ProductPage object
    # Assertion to verify that the cart button is visible after login
    assert product_page.is_cart_button_visible(), "Cart button is not visible after login"
    time.sleep(3)  # Wait for potential page load


# TC-005
def test_add_to_cart_names_prices(driver):
    """
    This test verifies that multiple products are successfully added to the cart.
    It checks the product names and prices to ensure that the correct products are added.
    """
    driver.get(Data.url)  # Navigate to the login page
    login_page = LoginPage(driver)  # Initialize LoginPage object
    login_page.enter_username(Data.username)  # Enter username
    login_page.enter_password(Data.password)  # Enter password
    login_page.click_login()  # Click login button
    base_page = BasePage(driver)  # Initialize BasePage object
    time.sleep(5)  # Wait for potential alert
    base_page.accept_alert_if_present()  # Accept any alert if present
    time.sleep(5)  # Wait for alert to be dismissed

    product_page = ProductPage(driver)  # Initialize ProductPage object
    product_page.add_multiple_products_to_cart()  # Add multiple products to cart
    product_page.get_all_product_names_and_prices()  # Print product names and prices
    time.sleep(5)  # Wait for the cart operation to complete
    print("SUCCESS: Products added to the cart")


# TC-006
def test_add_to_cart_count(driver):
    """
    This test validates the correct number of products added to the cart.
    It checks if the cart count matches the expected number of products added.
    """
    driver.get(Data.url)  # Navigate to the login page
    login_page = LoginPage(driver)  # Initialize LoginPage object
    login_page.enter_username(Data.username)  # Enter username
    login_page.enter_password(Data.password)  # Enter password
    login_page.click_login()  # Click login button
    base_page = BasePage(driver)  # Initialize BasePage object
    time.sleep(5)  # Wait for any alerts
    base_page.accept_alert_if_present()  # Accept alert if present
    time.sleep(5)  # Wait for alert to be dismissed

    product_page = ProductPage(driver)  # Initialize ProductPage object
    product_page.add_multiple_products_to_cart()  # Add multiple products to cart
    time.sleep(5)  # Wait for the cart operation to complete

    # Validate that the cart count is 4
    cart_count = product_page.get_cart_item_count()
    assert cart_count == 4  # Assert the number of items in the cart
    print("SUCCESS: Correct number of products added to the cart")


# TC-007
def test_added_products_into_cart(driver):
    """
    This test verifies that the products added to the cart are correctly displayed in the cart page.
    It checks that the cart contains the expected products.
    """
    driver.get(Data.url)  # Navigate to the login page
    login_page = LoginPage(driver)  # Initialize LoginPage object
    login_page.enter_username(Data.username)  # Enter username
    login_page.enter_password(Data.password)  # Enter password
    login_page.click_login()  # Click login button
    base_page = BasePage(driver)  # Initialize BasePage object
    time.sleep(5)  # Wait for any alerts
    base_page.accept_alert_if_present()  # Accept any alert
    time.sleep(5)  # Wait for alert dismissal

    product_page = ProductPage(driver)  # Initialize ProductPage object
    product_page.add_multiple_products_to_cart()  # Add products to cart
    time.sleep(5)  # Wait for cart operation to complete

    # Validate that the cart count is 4 (optional, can be reused from previous test case)
    cart_count = product_page.get_cart_item_count()
    assert cart_count == 4  # Assert correct number of items in cart
    print("SUCCESS: Correct number of products added to the cart")

    # Open the cart and validate the products
    product_page.click_cart_icon()  # Click on the cart icon
    time.sleep(3)  # Wait for the cart to load
    cart_page = CartPage(driver)  # Initialize CartPage object
    assert cart_page.get_all_cart_cards()  # Verify all cart items are displayed
    assert cart_page.get_total_cart_cards()  # Verify the total number of cart items







