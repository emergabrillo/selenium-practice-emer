from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators for the login page elements
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")

    def enter_username(self, username):
        """Enters the username into the username input field."""
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enters the password into the password input field."""
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Clicks the login button to submit the form."""
        self.click_element(self.SUBMIT_BUTTON)