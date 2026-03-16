from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_non_admin_access_restriction(driver):

    driver.get("https://react-frontend-api-testing.vercel.app/login")

    login_page = LoginPage(driver)

    # login as normal user
    login_page.login("john@example.com", "User@123")

    dashboard = DashboardPage(driver)

    # Users menu should NOT exist
    assert dashboard.users_menu_visible() is False