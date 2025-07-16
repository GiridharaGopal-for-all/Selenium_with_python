import time

from selenium.webdriver.common.by import By


class Login_fn():

    def __init__(self,driver):
        self.driver=driver

    def Username_Password(self,user,passw):
        self.driver.find_element(By.XPATH, '//*[@name="username"]').clear()
        self.driver.find_element(By.XPATH,'//*[@name="username"]').send_keys(user)
        self.driver.find_element(By.CSS_SELECTOR, '#password').clear()
        self.driver.find_element(By.CSS_SELECTOR,'#password').send_keys(passw)
        self.driver.find_element(By.CSS_SELECTOR,'.btn.btn-info.btn-md').click()
        time.sleep(5)

