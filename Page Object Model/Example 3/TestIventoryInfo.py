import unittest
from selenium import webdriver
from Page import InventoryPage
from Page import LoginPage
from Page import InventoryInfoPage
from selenium.webdriver.firefox.options import Options


class TestIventoryInfo(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.driver = webdriver.Firefox(
            executable_path=r'C:\Program Files (x86)\geckodriver.exe',
            options=options)
        self.driver.get("https://www.saucedemo.com/")

    def test_inventory_info(self):

        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        inventory_info_page = InventoryInfoPage(self.driver)

        # Login
        login_page.login("standard_user", "secret_sauce")
        login_page.click_login_button()

        # Login success
        self.assertTrue(inventory_page.check_title(), "Error!")

        # Backpack
        inventory_page.backpack_info()
        self.assertTrue(inventory_info_page.check_backpack(), "Error")
        inventory_info_page.back_to_product()
        self.assertTrue(inventory_page.check_title(), "Error!")

        # Bike Light
        inventory_page.bikelight_info()
        self.assertTrue(inventory_info_page.check_bikelight(), "Error")
        inventory_info_page.back_to_product()
        self.assertTrue(inventory_page.check_title(), "Error!")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
