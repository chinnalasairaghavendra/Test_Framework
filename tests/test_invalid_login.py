import pytest 
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "email,password",
    [
        ("admin@example.com", "wrongpassword"),
        ("wrongemail", "password"),
        ("", ""),
    ],
)
def test_invalid_login(driver, email, password):

    driver.get("https://react-frontend-api-testing.vercel.app/login")

    login_page = LoginPage(driver)

    login_page.login(email, password)

    assert "login" in driver.current_url.lower()