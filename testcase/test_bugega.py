
from page.cm.test_click_age import TestClickAge
from public.GetDriver import mydriver
from public.StartAppiumServer import Sp
import time,unittest

driver = mydriver()
appiumsevear = Sp(driver)

class Test_Click_Age(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit
        pass

    def test_cm_001(self):
        cm = TestClickAge(driver)
        cm.clickage()

if __name__ == "__main__":
    unittest.main()