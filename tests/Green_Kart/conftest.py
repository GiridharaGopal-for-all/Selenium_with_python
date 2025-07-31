import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pytest_html import extras


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



import pytest
import os
from pytest_html import extras

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = getattr(item.cls, "driver", None)
        if driver is not None:
            screenshot_dir = "tests/Screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            file_name = report.nodeid.replace("::", "_").replace("/", "_") + ".png"
            screenshot_path = os.path.join(screenshot_dir, file_name)
            driver.save_screenshot(screenshot_path)

            # ✅ Embed screenshot inline using extras.embed
            with open(screenshot_path, "rb") as image_file:
                image_bytes = image_file.read()
            extra_image = extras.embed(image_bytes, mime_type="image/png", extension="png")

            if hasattr(report, "extra"):
                report.extra.append(extra_image)
            else:
                report.extra = [extra_image]







