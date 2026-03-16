from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProjectsPage(BasePage):

    PROJECTS_MENU = (By.XPATH, "//a[text()='Projects']")
    NEW_PROJECT_BUTTON = (By.XPATH, "//button[contains(text(),'New Project')]")

    TITLE_INPUT = (By.XPATH, "//label[text()='Title']/following-sibling::input")
    DESCRIPTION_INPUT = (By.XPATH, "//label[text()='Description']/following-sibling::textarea")

    STATUS_SELECT = (By.CLASS_NAME, "form-select")

    SAVE_BUTTON = (By.XPATH, "//button[@type='submit' and  text()='Save']")

    PROJECT_TABLE = (By.TAG_NAME, "table")
    
    SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(text(),'Project created successfully')]"
    )

    def open_projects(self):
        self.click(self.PROJECTS_MENU)

    def open_new_project_modal(self):
        self.click(self.NEW_PROJECT_BUTTON)

    def create_project(self, title, description):

        self.enter_text(self.TITLE_INPUT, title)

        self.enter_text(self.DESCRIPTION_INPUT, description)

        self.click(self.SAVE_BUTTON)

    def project_table_visible(self):

        return self.is_visible(self.PROJECT_TABLE)
    

    def wait_for_project_creation(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )

    def project_exists(self, project_name):
        project_locator = (
            By.XPATH,
            f" //table//td[contains(.,'{project_name}')]"
        )
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(project_locator)
            )
            return True
        except:
            return False
        