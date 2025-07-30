import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class mobile():

    def __init__(self,driver):
        self.driver=driver
        self.multiple='(//div[@class="card-body"])//h4//a'

    def select_mobiles1(self):
        q=self.driver.find_elements(By.XPATH,self.multiple)
        for i in range(1,len(q)):
            w=self.driver.find_element(By.XPATH, '(//div[@class="card-body"])['+str(i)+']//h4//a').text
            if w=="Nokia Edge" :
                self.driver.find_element(By.XPATH,'(//*[@class="btn btn-info"])['+str(i)+']').click()
                time.sleep(4)
                break

    def select_mobiles(self):
        cards = self.driver.find_elements(By.XPATH, '//div[@class="card-body"]')
        for card in cards:
            title = card.find_element(By.XPATH, './/h4//a').text
            if title == "Nokia Edge":
                btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, './/button[contains(@class,"btn-info")]')))
                btn.click()
                break

    def verifying_text(self):
        if "Copyright © ProtoCommerce 2018" in self.driver.page_source:
            print("available")
        else:
            print("not available")
