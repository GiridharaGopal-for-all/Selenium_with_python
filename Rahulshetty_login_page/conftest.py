import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Rahulshetty_login_page import data


@pytest.fixture(scope='class')
def webbrowser(request):
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    request.cls.driver=driver
    yield
    driver.close()


@pytest.fixture(params=[{"user":"rahulshettyacademy","passw":"giri"},
                        {"user":"giri1","passw":"learning"},
                        {"user":"rahulshettyacademy","passw":"learning"}])

def login_values(request):
    return request.param

def login_datas():
    return["rahulshettyacademy","learning"]


def csv():
    data_list=[]
    with open("E:\\Giri\\test_purpose.txt") as f:
       lines=f.readlines()
    for line in lines:
        parts = line.strip().split()
        username=parts[1]
        password=parts[3]
        data_list.append((username,password))
    return data_list


@pytest.fixture(params=data.names)
def data(request):
    return request.param









