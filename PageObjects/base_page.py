"""
This BasePage class includes common utility methods like find_element, click, etc.
It serves as a parent class for different pages such as LoginPage, HomePage, and SignupPage,
enabling code reuse and centralized control over element interaction logic.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, NoSuchElementException

class BasePage:

    def __init__(self, driver):
        # Initialize with WebDriver instance and a default timeout for element wait
        self.driver = driver
        self.timeout = 15

    def find_element(self, locator):
        """
        Waits for a single element to be present in the DOM and returns it.
        """
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
            return web_element
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException) as error:
            print("ERROR: ", error)

    def find_elements(self, locator):
        """
        Waits for all matching elements to be present in the DOM and returns them as a list.
        """
        try:
            web_elements = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return web_elements
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException) as error:
            print("ERROR: ", error)

    def is_visible(self, locator):
        """
        Checks if an element is visible on the page.
        Returns True if visible, False otherwise.
        """
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return web_element.is_displayed()
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException) as error:
            print("ERROR: ", error)

    def is_clickable(self, locator):
        """
        Checks if an element is clickable and returns the element.
        """
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return web_element
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException) as error:
            print("ERROR: ", error)

    def click(self, locator):
        """
        Finds an element and clicks on it.
        """
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """
        Clears any existing text in the input field and enters new text.
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def fetch_title(self):
        """
        Returns the title of the current page.
        """
        return self.driver.title

    def fetch_url(self):
        """
        Returns the URL of the current page.
        """
        return self.driver.current_url

    def accept_alert_if_present(self, timeout=5):
        """
        Waits for an alert to be present and accepts it if found.
        Useful for handling pop-up alerts.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print(f"Alert text: {alert.text}")
            alert.accept()
            print("Alert accepted successfully.")
        except TimeoutException:
            print("No alert present within timeout.")
