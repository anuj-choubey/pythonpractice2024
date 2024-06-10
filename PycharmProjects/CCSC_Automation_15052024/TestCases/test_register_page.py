import pytest
import softest
from CCSC_Automation_15052024.Pages.registered import Register_page_code
from ddt import ddt, data, unpack
from CCSC_Automation_15052024.Utilities.utilities import utilities


@pytest.mark.usefixtures("setup")
@ddt
class Test_register_page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.register_page_code = Register_page_code(self.driver)

    @data(*utilities.read_data_from_excel(
        "C:\\Users\\Anuj\\Downloads\\CCSC_Automation_15052024\\CCSC_Automation_15052024\\TestData\\Book1.xlsx",
        "Sheet1"))
    @unpack
    def test_register_page_tc(self, name):
        self.register_page_code.tc28(name)
