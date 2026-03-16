from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger(__name__)


def test_valid_admin_login(driver):

    logger.info("Opening login page")

    driver.get("https://react-frontend-api-testing.vercel.app/login")

    login_page = LoginPage(driver)

    logger.info("Entering credentials")

    login_page.login("admin@example.com", "Admin@123")

    logger.info("Checking dashboard visibility")

    assert login_page.dashboard_visible()




