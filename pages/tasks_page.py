from selenium.webdriver.common.by import By
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

    PROJECT_DROPDOWN = (
        By.CSS_SELECTOR,
        "select.form-select"
    )

    # first real project (skip "Select project")
    PROJECT_OPTION = (
        By.XPATH,
        "//select[contains(@class,'form-select')]/option[2]"
    )

    SAVE_TASK_BUTTON = (By.XPATH, "//button[contains(text(),'Save Task')]")

    STATUS_CELL = (
        By.CSS_SELECTOR,
        "table tbody tr:first-child td:nth-child(3)"
    )


    def open_tasks(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable(self.TASKS_MENU)
        ).click()


    def edit_first_task(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable(self.EDIT_TODO_TASK)
        ).click()


    def change_status(self, status):

        dropdown = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable(self.STATUS_DROPDOWN)
        )
        dropdown.send_keys(status)


    def select_project(self):

        print("Selecting project from modal")

        dropdown = WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located(self.PROJECT_DROPDOWN)
        )

        # scroll into view (important for CI/headless)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)

        # use Select (more reliable for <select>)
        from selenium.webdriver.support.ui import Select
        select = Select(dropdown)

        select.select_by_index(1)   # skip "Select project"


    def save_task(self):

        self.select_project()

        print("Click Save Task")

        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable(self.SAVE_TASK_BUTTON)
        ).click()


    def get_task_status(self):
        return self.get_text(self.STATUS_CELL)