import unittest
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from Page import InventoryPage
from Page import LoginPage
from Page import CartPage


class TestAddToCart(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.driver = webdriver.Firefox(
            executable_path=r'C:\Program Files (x86)\geckodriver.exe',
            options=options)
        self.driver.get("https://www.saucedemo.com/")

    def test_add_to_cart(self):

        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver)

        # Login
        login_page.login("standard_user", "secret_sauce")
        login_page.click_login_button()

        # Check login success
        self.assertTrue(inventory_page.check_title(), "Error!")

        # Add Back Pack to Cart
        inventory_page.add_backpack()

        # Check add back pack success at inventory page
        self.assertTrue(inventory_page.check_add_backpack_success(), "Error!")

        # Go to cart page
        inventory_page.go_to_cart()

        # Check go to cart page success
        self.assertTrue(cart_page.check_in, "Error!")

        # Check back pack is included in the cart page
        self.assertTrue(cart_page.check_backpack, "Error!")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
