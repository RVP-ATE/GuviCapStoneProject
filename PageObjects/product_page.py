"""
This file contains methods related to the product page, including interacting with product cards,
adding products to the cart, sorting, and fetching product details.
"""

from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocator.locators import Locators
from selenium.webdriver.support.ui import Select
import random
from selenium.common.exceptions import NoAlertPresentException
import time
from Configuration.conftest import driver

class ProductPage(BasePage):
    # Locators for product page elements
    PRODUCT_CARDS = (By.CLASS_NAME, Locators.product_card_locator)        # Locator for product card container
    SORT_DROPDOWN = (By.CLASS_NAME, Locators.sort_dropdown_locator)      # Locator for sort dropdown menu
    PRODUCT_PRICE = (By.CLASS_NAME, Locators.product_price_locator)      # Locator for product price
    PRODUCT_NAME = (By.CLASS_NAME, Locators.product_name_locator)        # Locator for product name
    ADD_TO_CART_BUTTON = (By.XPATH, Locators.add_to_cart_button_locator) # XPATH for add to cart button
    CART_ICON = (By.XPATH, Locators.cart_icon_locator)                   # XPATH for cart icon
    REMOVE_BUTTON = (By.XPATH, Locators.remove_button_locator)          # XPATH for remove button on product cards
    OPEN_MENU = (By.XPATH, Locators.menu)                                # XPATH for menu button
    MENU_LIST = (By.XPATH, Locators.menu_list)                           # XPATH for menu list
    LOGOUT = (By.XPATH, Locators.logout)                                 # XPATH for logout link in the menu

    def get_all_product_cards(self):
        """
        Returns the element containing all product cards on the page.
        """
        return self.find_element(self.PRODUCT_CARDS)

    def get_total_product_cards(self):
        """
        Returns the total number of product cards displayed on the page.
        """
        return len(self.find_elements(self.PRODUCT_CARDS))

    def select_sort_option(self, option_text):
        """
        Selects a sorting option from the sort dropdown based on visible text.

        Args:
            option_text (str): The visible text of the sorting option to select.
        """
        dropdown_element = self.is_clickable(self.SORT_DROPDOWN)

        # Create a select object to choose by visible text
        select = Select(dropdown_element)
        select.select_by_visible_text(option_text)

    def get_product_prices(self):
        """
        Fetches all product prices from the page, cleans the data and returns a list of float values.

        Returns:
            List[float]: A list of product prices as floats.
        """
        price_elements = self.find_elements(self.PRODUCT_PRICE)
        prices = []
        for element in price_elements:
            price = element.text.strip()
            number = float(price.replace('$', ''))  # Removes dollar sign and converts to float
            prices.append(number)
        return prices

    def add_multiple_products_to_cart(self, count=4):
        """
        Randomly selects a specified number of products from the available products and adds them to the cart.

        Args:
            count (int): The number of products to add to the cart (default is 4).
        """
        cards = self.find_elements(self.PRODUCT_CARDS)
        product_names = []

        # Extract all product names from the page
        for card in cards:
            name_element = card.find_element(*self.PRODUCT_NAME)
            product_names.append(name_element.text.strip())

        # Randomly select 'count' products
        selected_products = random.sample(product_names, count)
        print(f"Selected products to add: {selected_products}")

        # Add the selected products to the cart
        for card in cards:
            try:
                name_element = card.find_element(*self.PRODUCT_NAME)
                product_name = name_element.text.strip()
                if product_name in selected_products:
                    add_button = card.find_element(*self.ADD_TO_CART_BUTTON)
                    add_button.click()
                    print(f"Added to cart: {product_name}")
            except Exception as e:
                print(f"Error adding product: {e}")

    def get_all_product_names_and_prices(self):
        """
        Fetches and returns a list of tuples containing product names and their corresponding prices.

        Returns:
            List[Tuple[str, str]]: A list of tuples where each tuple contains the product name and price.
        """
        products = []
        cards = self.find_elements(self.PRODUCT_CARDS)

        for card in cards:
            try:
                name_element = card.find_element(*self.PRODUCT_NAME)
                price_element = card.find_element(*self.PRODUCT_PRICE)

                name = name_element.text.strip()
                price = price_element.text.strip()

                products.append((name, price))
                print(f"Product: {name}, Price: {price}")

            except Exception as e:
                print(f"Error fetching product info: {e}")

        return products

    def get_cart_item_count(self):
        """
        Retrieves the number of items in the cart.

        Returns:
            int: The count of items in the cart.
        """
        count_item = self.find_element(self.CART_ICON).text.strip()
        return int(count_item) if count_item.isdigit() else 0

    def click_remove_by_product_name(self):
        """
        Clicks the remove button for a product in the cart.
        """
        remove_button = self.find_element(self.REMOVE_BUTTON)
        remove_button.click()

    def click_cart_icon(self):
        """
        Clicks on the cart icon to navigate to the cart page.
        """
        self.click(self.CART_ICON)

    def is_cart_button_visible(self):
        """
        Checks whether the cart button is visible on the page.

        Returns:
            bool: True if the cart button is visible, False otherwise.
        """
        return self.is_visible(self.CART_ICON)

    def click_menu(self):
        """
        Opens the menu by clicking the menu button.
        """
        self.click(self.OPEN_MENU)

    def logout(self):
        """
        Logs the user out by clicking the logout option in the menu.
        """
        if self.is_visible(self.MENU_LIST):
            self.click(self.LOGOUT)
            print("Logout successful")
        else:
            print("Logout failed: Menu list not visible")
