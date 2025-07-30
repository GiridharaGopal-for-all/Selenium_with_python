import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By




class Test_try():

    def test_element(self,tesstdata):
            self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.get("https://leafground.com/table.xhtml")
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            country=self.driver.find_elements(By.XPATH,'//*[@id="form:j_idt89_data"]//tr//td[2]')
            pages=self.driver.find_elements(By.XPATH,'//*[@class="ui-paginator-pages"]//a')
            for i in range(1,len(pages)+1):
                self.driver.find_element(By.XPATH, '//*[@class="ui-paginator-pages"]//a['+str(i)+']').click()
                count=0
                for i in range (1,len(country)):
                    country_name=self.driver.find_element(By.XPATH, '//*[@id="form:j_idt89_data"]//tr['+str(i)+']//td[2]').text
                    if country_name== "Brazil":
                        Name=self.driver.find_element(By.XPATH, '//*[@id="form:j_idt89_data"]//tr[' + str(i) + ']//td[3]').text
                        Date=self.driver.find_element(By.XPATH, '//*[@id="form:j_idt89_data"]//tr['+str(i)+']//td[4]').text
                        print(f'{Name}:{Date}')
                    else:
                        self.driver.switch_to.default_content()




