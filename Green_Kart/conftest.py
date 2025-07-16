import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService


@pytest.fixture(params=["Chrome","Edge"],scope="class")
def browsers(request):
    browser=request.param
    if browser=="Chrome":
        driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    elif browser=="Edge":
        service = EdgeService(executable_path=r"C:\Users\Devils Den\msedgedriver.exe")
        driver = webdriver.Edge(service=service)

    else :
            driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()



