from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from config.settings import Config


def get_driver():

    options = Options()

    # Headless mode for CI environments
    if Config.HEADLESS:
        options.add_argument("--headless=new")

    # Required for Docker / Jenkins
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")

    # If running on Selenium Grid
    if Config.GRID_URL:
        driver = webdriver.Remote(
            command_executor=Config.GRID_URL,
            options=options
        )

    # Run locally
    else:
        service = Service()   # Selenium manager auto handles chromedriver
        driver = webdriver.Chrome(service=service, options=options)

    return driver