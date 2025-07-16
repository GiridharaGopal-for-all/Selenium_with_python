import pytest
from selenium.webdriver.common.by import By

from Green_Kart.Pages.Homepage import Homepage
from Rahulshetty_login_page.Pages.Cart import Cart


@pytest.mark.usefixtures("browsers")
class Test_green():

    def test_main(self):
        homepg= Homepage(self.driver)
        homepg.add_products()
        homepg.click_on_cart()

        cartpg=Cart(self.driver)
        cartpg.verifying_price()
        cartpg.place_order()
        cartpg.country()
        cartpg.verfiication()

