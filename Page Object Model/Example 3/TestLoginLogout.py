import unittest
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from Page import InventoryPage
from Page import LoginPage


class TestLoginLogout(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.driver = webdriver.Firefox(
            executable_path=r'C:\Program Files (x86)\geckodriver.exe',
            options=options)
        self.driver.get("https://www.saucedemo.com/")

    def test_login_logout(self):

        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)

        login_page.login("standard_user", "secret_sauce")
        login_page.click_login_button()

        self.assertTrue(inventory_page.check_title(), "Error!")

        inventory_page.logout()

        self.assertTrue(login_page.check_in(), "Error!")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
