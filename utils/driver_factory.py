from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import Config


def get_driver():

    options = Options()

    if Config.HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")

    if Config.GRID_URL:

        driver = webdriver.Remote(
            command_executor=Config.GRID_URL,
            options=options
        )

    else:

        driver = webdriver.Chrome(options=options)

    return driver