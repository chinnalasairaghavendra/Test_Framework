from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TasksPage(BasePage):

    TASKS_MENU = (By.XPATH, "//a[text()='Tasks']")

    EDIT_TODO_TASK = (
        By.XPATH,
        "(//table//tr//button[contains(text(),'Edit')])[1]"
    )  

    STATUS_DROPDOWN = (
    By.XPATH,
    "//label[text()='Status']/following::select[1]"
    )

    SAVE_TASK_BUTTON = (By.XPATH, "//button[contains(text(),'Save Task')]")

    STATUS_CELL = (
        By.XPATH,
        "(//table//tbody//tr)[1]/td[3]"
    )

    def open_tasks(self):
        self.click(self.TASKS_MENU)

    def edit_first_task(self):
        self.click(self.EDIT_TODO_TASK)

    def change_status(self, status):

        dropdown = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.STATUS_DROPDOWN)
        )
        Select(dropdown).select_by_value(status)

    def save_task(self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.SAVE_TASK_BUTTON)
        ).click()
        # wait until modal disappears
        WebDriverWait(self.driver,10).until(
            EC.invisibility_of_element_located(self.SAVE_TASK_BUTTON)
        )

    def get_task_status(self):
        return self.get_text(self.STATUS_CELL)