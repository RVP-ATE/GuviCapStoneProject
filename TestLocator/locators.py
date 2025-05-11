"""
This file contains all the web element locators such as XPath, ID, class name, etc.
Centralizing locators makes the framework easier to update and maintain.
"""

class Locators:

    # ---------------------------
    # Login Page Locators
    # ---------------------------
    username_locator = "user-name"                     # ID for username input field
    password_locator = "password"                      # ID for password input field
    login_button_locator = "login-button"              # ID for login button

    # ---------------------------
    # Products Page Locators
    # ---------------------------
    product_card_locator = "inventory_item"            # CLASS NAME for individual product card container
    sort_dropdown_locator = "product_sort_container"   # CLASS NAME for sorting dropdown
    product_price_locator = "inventory_item_price"     # CLASS NAME for product price text
    product_name_locator = "inventory_item_name "      # CLASS NAME for product name (note: extra space to verify)
    add_to_cart_button_locator = "//button[contains(text(), 'Add to cart')]"  # XPATH for any 'Add to cart' button
    cart_icon_locator = "//*[@id='shopping_cart_container']"  # XPATH for cart icon
    remove_button_locator = "//button[contains(text(), 'Remove')]"            # XPATH for 'Remove' button
    menu = "//button[text()='Open Menu']"               # XPATH for burger menu button
    menu_list = "//*[@class='bm-item-list']"            # XPATH for menu list container
    logout = "//a[text()='Logout']"                     # XPATH for Logout link in menu

    # ---------------------------
    # Cart Page Locators
    # ---------------------------
    cart_contents_container = "//*[@id='cart_contents_container']"  # XPATH for entire cart content section
    inventory_item_name = "//*[@class='inventory_item_name']"       # XPATH for item names in the cart
    checkout = "//*[@id='checkout']"                                # XPATH for checkout button

    # ---------------------------
    # Checkout Page Locators
    # ---------------------------
    first_name = "//*[@id='first-name']"                # XPATH for first name input field
    last_name = "//*[@id='last-name']"                  # XPATH for last name input field
    zip_postalcode = "//*[@id='postal-code']"           # XPATH for ZIP/postal code field
    continue_checkout = "//*[@id='continue']"           # XPATH for continue button in checkout
    checkout_cart = "//*[@class='cart_list']"           # XPATH for list of items on the checkout page
    finish = "//*[@id='finish']"                        # XPATH for finish button to complete the order

    # ---------------------------
    # Order Completion Page
    # ---------------------------
    checkout_complete = "//*[text()='Thank you for your order!']"   # XPATH for order confirmation message
