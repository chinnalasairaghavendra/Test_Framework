from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):

    USERS_MENU = (By.XPATH, "//a[contains(text(),'Users')]")

    def go_to_users(self):

        self.click(self.USERS_MENU)
    
    def users_menu_visible(self):
        elements = self.driver.find_elements(*self.USERS_MENU)
        return len(elements) > 0