"""
LoginPage contains methods related to login actions.
It inherits common methods from BasePage and uses locators defined in the Locators class.
"""

from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocator.locators import Locators

class LoginPage(BasePage):
    # Define element locators for login page using IDs from Locators
    USERNAME_INPUT = (By.ID, Locators.username_locator)           # Username input field
    PASSWORD_INPUT = (By.ID, Locators.password_locator)           # Password input field
    LOGIN_BUTTON = (By.ID, Locators.login_button_locator)         # Login button

    def enter_username(self, username):
        """
        Enters the provided username into the username input field.
        """
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """
        Enters the provided password into the password input field.
        """
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """
        Clicks the login button.
        """
        self.click(self.LOGIN_BUTTON)

    def validate_username(self):
        """
        Validates that the username input field is visible on the page.
        Returns True if visible, else False.
        """
        return self.is_visible(self.USERNAME_INPUT)

    def validate_password(self):
        """
        Validates that the password input field is visible on the page.
        Returns True if visible, else False.
        """
        return self.is_visible(self.PASSWORD_INPUT)

    def is_login_button_displayed(self):
        """
        Validates that the login button is visible on the page.
        Returns True if visible, else False.
        """
        return self.is_visible(self.LOGIN_BUTTON)

    def login(self, username, password):
        """
        Performs the full login sequence by entering username, password,
        and clicking the login button.
        """
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
