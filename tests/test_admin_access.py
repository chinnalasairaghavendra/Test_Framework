from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.users_page import UsersPage
from utils.logger import get_logger

logger = get_logger(__name__)

def test_admin_users_page_access(driver):

    driver.get("https://react-frontend-api-testing.vercel.app/login")

    login_page = LoginPage(driver)

    login_page.login("admin@example.com", "Admin@123")

    dashboard = DashboardPage(driver)

    dashboard.go_to_users()

    users_page = UsersPage(driver)

    assert users_page.users_table_visible()