import base64
from PIL import Image
import io
from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocator.locators import Locators
import time

class CheckPage(BasePage):
    # Define locators for checkout form fields and buttons using XPATH from the Locators class
    FIRST_NAME = (By.XPATH, Locators.first_name)             # Input field for first name
    LAST_NAME = (By.XPATH, Locators.last_name)               # Input field for last name
    ZIP_CODE = (By.XPATH, Locators.zip_postalcode)           # Input field for ZIP/postal code
    CONTINUE = (By.XPATH, Locators.continue_checkout)        # Button to proceed in the checkout
    CHECKOUT_CART = (By.XPATH, Locators.checkout_cart)       # Section showing cart items during checkout
    FINISH = (By.XPATH, Locators.finish)                     # Button to complete the checkout
    COMPLETE = (By.XPATH, Locators.checkout_complete)        # Element indicating successful order completion

    def enter_firstname(self, firstname):
        """
        Enters the provided first name into the first name input field.
        """
        self.enter_text(self.FIRST_NAME, firstname)

    def enter_lastname(self, lastname):
        """
        Enters the provided last name into the last name input field.
        """
        self.enter_text(self.LAST_NAME, lastname)

    def enter_zipcode(self, zipcode):
        """
        Enters the provided ZIP code into the ZIP code input field.
        """
        self.enter_text(self.ZIP_CODE, zipcode)

    def click_continue(self):
        """
        Clicks the 'Continue' button to proceed in the checkout process.
        """
        self.click(self.CONTINUE)

    def take_screenshot(self, file_path="checkout_overview.png"):
        """
        Takes a screenshot of the current page and saves it to a file.
        The screenshot is captured in base64 format and converted using PIL.
        """
        time.sleep(2)  # Wait to ensure page content is fully loaded

        # Get screenshot in base64 format
        screenshot_base64 = self.driver.get_screenshot_as_base64()
        image_data = base64.b64decode(screenshot_base64)

        # Convert base64 image to an actual image and save it
        image = Image.open(io.BytesIO(image_data))
        image.save(file_path)
        print(f"Screenshot saved at {file_path}")

    def verify_checkout_items(self):
        """
        Verifies that the checkout items section is present.
        Returns the WebElement for further inspection if needed.
        """
        return self.find_element(self.CHECKOUT_CART)

    def click_finish(self):
        """
        Scrolls the page and clicks the 'Finish' button to complete the order.
        """
        self.driver.execute_script("window.scrollBy(0, 500)")  # Ensure button is in view
        self.click(self.FINISH)

    def verify_complete_checkout(self):
        """
        Checks if the checkout completion message or section is visible.
        Returns True if visible, False otherwise.
        """
        return self.is_visible(self.COMPLETE)


