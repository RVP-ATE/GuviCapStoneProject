from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocator.locators import Locators

class CartPage(BasePage):
    # Define locators for cart elements using XPATH from a centralized Locators class
    CART_CONTENTS = (By.XPATH, Locators.cart_contents_container)  # Locator for the container that holds cart items
    CART_INVENTORY = (By.XPATH, Locators.inventory_item_name)      # Locator for individual item names in the cart
    CHECKOUT = (By.XPATH, Locators.checkout)                       # Locator for the checkout button

    def get_all_cart_cards(self):
        """
        Returns the cart contents container WebElement.
        Useful for verifying if the cart section is displayed.
        """
        return self.find_element(self.CART_CONTENTS)

    def get_total_cart_cards(self):
        """
        Returns the total number of items (cards) present in the cart.
        Uses the presence of all elements matching the CART_CONTENTS locator.
        """
        return len(self.find_elements(self.CART_CONTENTS))

    def click_checkout(self):
        """
        Scrolls the window down by 500 pixels and clicks the checkout button.
        Useful if the button is not initially visible on the screen.
        """
        self.driver.execute_script("window.scrollBy(0, 500)")  # Scroll to make the button visible
        self.click(self.CHECKOUT)







