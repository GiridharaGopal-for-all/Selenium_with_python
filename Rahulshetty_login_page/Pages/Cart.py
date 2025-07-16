from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Cart():

    def __init__(self,driver):
        self.driver=driver

    def verifying_price(self):
        rows = self.driver.find_elements(By.XPATH, '//table[@class="cartTable"]/tbody/tr')
        total_price = 0
        for row in rows:
            product_name = row.find_element(By.XPATH, './td[2]/p').text
            price_text = row.find_element(By.XPATH, './td[4]').text
            if product_name in ["Brocolli - 1 Kg", "Carrot - 1 Kg"]:
                total_price += int(price_text)
        print("Total price of Brocolli and Carrot is:", total_price)

        total_price1=176
        assert total_price1==total_price

    def place_order(self):
        self.driver.find_element(By.XPATH,'//*[text()="Place Order"]').click()

    def country(self):
        value=Select(self.driver.find_element(By.XPATH,"//label[text()='Choose Country']/following::select[1]"))
        value.select_by_visible_text("India")

    def verfiication(self):
        self.driver.find_element(By.XPATH,'//*[text()="Proceed"]').click()
        error="Please accept Terms & Conditions - Required"
        r=self.driver.find_element(By.XPATH,"//*[@class='errorAlert']/b").text
        assert error == r
