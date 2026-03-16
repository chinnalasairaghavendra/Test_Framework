import pytest
from utils.driver_factory import get_driver
from utils.screenshot_utils import capture_screenshot
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.fixture()
def driver():

    driver = get_driver()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        if report.passed:
            logger.info(f"TEST PASSED: {item.name}")

        elif report.failed:
            logger.error(f"TEST FAILED: {item.name}")

            driver = item.funcargs.get("driver")

            if driver:
                capture_screenshot(driver, item.name)

        elif report.skipped:
            logger.warning(f"TEST SKIPPED: {item.name}")