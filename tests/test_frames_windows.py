from pages.login_page import LoginPage
from pages.test_scenarios_page import TestScenariosPage


def test_frames_and_windows(driver):

    driver.get("https://react-frontend-api-testing.vercel.app/login")

    login_page = LoginPage(driver)
    login_page.login("john@example.com", "User@123")

    scenarios = TestScenariosPage(driver)

    scenarios.open_test_scenarios()

    driver.switch_to.frame("test-iframe")

    assert "Example Domain" in driver.page_source

    driver.switch_to.default_content()

    scenarios.open_new_tab()

    driver.switch_to.window(driver.window_handles[1])

    assert "Example Domain" in driver.title

    driver.close()

    driver.switch_to.window(driver.window_handles[0])