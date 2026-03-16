from pages.base_page import BasePage
from config.locators import LoginLocators


class LoginPage(BasePage):

    def login(self, email, password):

        self.enter_text(LoginLocators.EMAIL, email)

        self.enter_text(LoginLocators.PASSWORD, password)

        self.click(LoginLocators.LOGIN_BUTTON)

    def dashboard_visible(self):

        return self.is_visible(LoginLocators.DASHBOARD_HEADER)

    def get_error_message(self):

        return self.get_text(LoginLocators.ERROR_MESSAGE)