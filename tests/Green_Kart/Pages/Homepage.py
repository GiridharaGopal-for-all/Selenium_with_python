import pytest
from selenium.webdriver.common.by import By




class Homepage():
    def __init__(self,driver):
        self.driver=driver




    def add_products(self,test_data):
        products = self.driver.find_elements(By.XPATH, '//div[@class="products"]//div//h4')
        for i in products:
            if i.text in test_data:
                add_button = self.driver.find_element(By.XPATH, f'//h4[text()="{i.text}"]//following-sibling::div//button')
                add_button.click()


    def click_on_cart(self):
        self.driver.find_element(By.XPATH,'//img[@alt="Cart"]').click()
        self.driver.find_element(By.XPATH,'//button[text()="PROCEED TO CHECKOUT"]').click()





