from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage


def test_create_project(driver):

    driver.get("https://react-frontend-api-testing.vercel.app/login")

    login_page = LoginPage(driver)
    login_page.login("john@example.com", "User@123")

    projects = ProjectsPage(driver)

    projects.open_projects()
    projects.open_new_project_modal()

    project_name = "Automation Test Project"

    projects.create_project(project_name, "Created by Selenium")

    projects.wait_for_project_creation()

    assert projects.project_exists(project_name)