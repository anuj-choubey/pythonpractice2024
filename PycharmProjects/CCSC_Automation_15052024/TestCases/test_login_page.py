import pytest
import softest
from CCSC_Automation_15052024.Pages.Login import Login_page_code
from ddt import ddt, data, unpack
from CCSC_Automation_15052024.Utilities.utilities import utilities


@pytest.mark.usefixtures("setup")
@ddt
class Test_login_page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login_page_code = Login_page_code(self.driver)

    @data(*utilities.read_data_from_excel(
        "C:\\Users\\Anuj\\Downloads\\CCSC_Automation_15052024\\CCSC_Automation_15052024\\TestData\\login_pageTC.xlsx",
        "Sheet1"))
    @unpack
    def test_login_page_tc(self, email, password, Cemail, Cpassword):
        self.login_page_code.all(email, password, Cemail, Cpassword)
