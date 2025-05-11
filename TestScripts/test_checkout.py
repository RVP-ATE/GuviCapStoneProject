import time
from PageObjects.cart_page import CartPage
from PageObjects.checkout_page import CheckPage
from PageObjects.login_page import LoginPage
from PageObjects.base_page import BasePage
from PageObjects.product_page import ProductPage
from TestData.data import Data
from Configuration.conftest import driver


# TC-008: Test checkout functionality

def test_checkout(driver):
    """
    This test checks the complete checkout flow from logging in, adding products to the cart,
    entering checkout details, and verifying the order completion message.
    """

    # Step 1: Navigate to the login page and log in
    driver.get(Data.url)  # Navigate to the test URL
    login_page = LoginPage(driver)  # Initialize the LoginPage object
    login_page.enter_username(Data.username)  # Enter the username for login
    login_page.enter_password(Data.password)  # Enter the password for login
    login_page.click_login()  # Click the login button

    # Step 2: Handle potential alerts that might appear after login
    base_page = BasePage(driver)  # Initialize the BasePage object
    time.sleep(5)  # Wait for potential page load or alert handling
    base_page.accept_alert_if_present()  # Accept any alert that appears
    time.sleep(5)  # Wait after accepting alert

    # Step 3: Add multiple products to the cart
    product_page = ProductPage(driver)  # Initialize the ProductPage object
    product_page.add_multiple_products_to_cart()  # Add 4 random products to the cart
    time.sleep(5)  # Wait for the products to be added to the cart

    # Step 4: Go to the cart page
    product_page.click_cart_icon()  # Click on the cart icon to navigate to the cart page
    time.sleep(3)  # Wait for the cart page to load

    # Step 5: Assert that the cart has items
    cart_page = CartPage(driver)  # Initialize the CartPage object
    assert cart_page.get_all_cart_cards()  # Assert that cart contains items
    assert cart_page.get_total_cart_cards()  # Assert that the number of items is correct

    # Step 6: Proceed to the checkout page
    cart_page.click_checkout()  # Click the checkout button to navigate to the checkout page
    time.sleep(3)  # Wait for the checkout page to load

    # Step 7: Fill out the checkout information
    checkout_page = CheckPage(driver)  # Initialize the CheckoutPage object
    checkout_page.enter_firstname(Data.firstname)  # Enter the first name
    checkout_page.enter_lastname(Data.lastname)  # Enter the last name
    checkout_page.enter_zipcode(Data.zipcode)  # Enter the zipcode
    checkout_page.click_continue()  # Click the continue button to proceed

    # Step 8: Take a screenshot of the checkout overview page for validation
    time.sleep(3)  # Wait for the page to load
    checkout_page.take_screenshot()  # Take a screenshot of the page

    # Step 9: Verify that the checkout items are present
    time.sleep(2)  # Wait a little before asserting
    assert checkout_page.verify_checkout_items()  # Assert that the checkout items are visible

    # Step 10: Complete the checkout by clicking the finish button
    checkout_page.click_finish()  # Click the finish button to complete the order
    time.sleep(2)  # Wait for the final page to load

    # Step 11: Verify that the checkout process is complete
    complete_message = checkout_page.verify_complete_checkout()  # Check for the completion message
    if complete_message:  # If the message is displayed, print it
        print(f"After clicking finish message: {complete_message}")
