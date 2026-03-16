from selenium.webdriver.common.by import By


class LoginLocators:

    EMAIL = (By.XPATH, "//input[@type='email']")

    PASSWORD = (By.XPATH, "//input[@type='password']")

    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    DASHBOARD_HEADER = (By.XPATH, "//h2[contains(text(),'Dashboard')]")

    ERROR_MESSAGE = (By.CLASS_NAME, "text-red-500")