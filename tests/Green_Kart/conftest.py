import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService


@pytest.fixture(params=["Chrome"],scope="class",autouse=True)
def browsers(request):
    browser=request.param
    if browser == "Chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)



    driver.implicitly_wait(12)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

import pytest
import os

# Hook to add screenshot for each test
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot on test call stage
    if report.when == "call":
        driver = item.cls.driver  # assumes self.driver is defined in test class

        screenshot_dir = "tests/Screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        screenshot_path = os.path.join(screenshot_dir, f"{report.nodeid.replace('::', '_')}.png")
        driver.save_screenshot(screenshot_path)

        # Attach to HTML report
        if hasattr(report, "extra"):
            from pytest_html import extras
            report.extra.append(extras.image(screenshot_path))
        else:
            report.extra = [extras.image(screenshot_path)]


# @pytest.fixture(params=testdata.vegetables)
# def test_data(request):
#     return request.param




