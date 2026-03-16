import os
from datetime import datetime


def capture_screenshot(driver, name):

    screenshot_dir = "reports/screenshots"

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = f"{screenshot_dir}/{name}_{timestamp}.png"

    driver.save_screenshot(file_path)

    return file_path