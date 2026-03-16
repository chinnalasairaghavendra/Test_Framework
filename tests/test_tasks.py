from pages.login_page import LoginPage
from pages.tasks_page import TasksPage


def test_task_status_update(driver):

    driver.get("https://react-frontend-api-testing.vercel.app/login")

    login_page = LoginPage(driver)
    login_page.login("john@example.com", "User@123")

    tasks = TasksPage(driver)

    tasks.open_tasks()

    tasks.edit_first_task()

    tasks.change_status("in_progress")

    tasks.save_task()

    driver.refresh()

    tasks.open_tasks()

    assert "in_progress" in tasks.get_task_status().lower()