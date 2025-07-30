import pytest

from Rahulshetty_login_page.Pages.Home import mobile
from Rahulshetty_login_page.Pages.Login import Login_fn
from Rahulshetty_login_page.conftest import login_datas, csv
from Rahulshetty_login_page.utilis import xl


@pytest.mark.usefixtures('webbrowser')
class Test_Rahul():

    def test_shetty_login(self,login_values):
        login = Login_fn(self.driver)
        login.Username_Password(login_values["user"], login_values["passw"])

    def test_selecting_mobiles(self):

            login = Login_fn(self.driver)
            login.Username_Password(login_datas()[0], login_datas()[1])
            mobiles_selection=mobile(self.driver)
            mobiles_selection.select_mobiles()


    @pytest.mark.parametrize("username,password",csv())
    def test_csv(self,username,password):

        login = Login_fn( self.driver)
        login.Username_Password(username,password)

    @pytest.mark.parametrize("username,password", xl.excel_data())
    def test_exceldata(self,username,password):
        login = Login_fn(self.driver)
        login.Username_Password(username, password)

    def test_testdatafile(self,data):
        login = Login_fn(self.driver)
        login.Username_Password(data["username"],data["password"])
        home=mobile(self.driver)
        home.verifying_text()


    



