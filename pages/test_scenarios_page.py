from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TestScenarioPage(BasePage):

    TEST_SCENARIOS_MENU = (By.XPATH, "//a[text()='Test Scenarios']")

    ALERT_BUTTON = (By.XPATH, "//button[contains(text(),'Trigger Alert')]")

    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Trigger Confirm')]")

    PROMPT_BUTTON = (By.XPATH, "//button[contains(text(),'Trigger Prompt')]")

    CONFIRM_RESULT = (By.ID, "confirm-result")

    PROMPT_RESULT = (By.ID, "prompt-result")

    def open_test_scenarios(self):
        self.click(self.TEST_SCENARIOS_MENU)

    def trigger_alert(self):
        self.click(self.ALERT_BUTTON)

    def trigger_confirm(self):
        self.click(self.CONFIRM_BUTTON)

    def trigger_prompt(self):
        self.click(self.PROMPT_BUTTON)

    def get_confirm_result(self):
        return self.get_text(self.CONFIRM_RESULT)

    def get_prompt_result(self):
        return self.get_text(self.PROMPT_RESULT)
    

    TEST_SCENARIOS_MENU = (By.XPATH, "//a[text()='Test Scenarios']")

    NEW_TAB_BUTTON = (By.ID, "btn-new-tab")

    POPUP_BUTTON = (By.ID, "btn-popup-window")

    IFRAME = (By.ID, "test-iframe")

    IFRAME_TEXT = (By.XPATH, "//h1[contains(text(),'Example Domain')]")

    def open_new_tab(self):
        self.click(self.NEW_TAB_BUTTON)

    def open_popup(self):
        self.click(self.POPUP_BUTTON)