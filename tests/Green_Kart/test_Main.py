from tests.Green_Kart import testdata
from tests.Green_Kart.Pages.Homepage import Homepage
from tests.Green_Kart.Pages.Cart import Cart


# @pytest.mark.usefixtures("browsers")
class Test_green():


    def test_main(self):
        homepg= Homepage(self.driver)
        homepg.add_products(testdata.vegetables)
        homepg.click_on_cart()

        cartpg=Cart(self.driver)
        cartpg.verifying_price()
        cartpg.place_order()
        cartpg.country()
        cartpg.verfiication()

