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

# @pytest.fixture(params=testdata.vegetables)
# def test_data(request):
#     return request.param




