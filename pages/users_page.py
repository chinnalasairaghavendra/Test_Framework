from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class UsersPage(BasePage):

    USERS_TABLE = (By.TAG_NAME, "table")

    def users_table_visible(self):

        return self.is_visible(self.USERS_TABLE)