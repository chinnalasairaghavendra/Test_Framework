from pages.login_page import LoginPage
from pages.test_scenarios_page import TestScenariosPage


def test_alerts_handling(driver):

    driver.get("https://react-frontend-api-testing.vercel.app/login")

    login_page = LoginPage(driver)
    login_page.login("admin@example.com", "Admin@123")

    scenarios = TestScenariosPage(driver)

    scenarios.open_test_scenarios()

    scenarios.trigger_alert()
    driver.switch_to.alert.accept()

    scenarios.trigger_confirm()
    driver.switch_to.alert.dismiss()

    assert "Cancelled" in scenarios.get_confirm_result()

    scenarios.trigger_prompt()

    alert = driver.switch_to.alert
    alert.send_keys("Automation")
    alert.accept()

    assert "Automation" in scenarios.get_prompt_result()