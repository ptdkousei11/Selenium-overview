from Locators import LoginPageLocators
from Locators import IventoryPageLocators
from Locators import InventoryInfoPageLocator
from BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_in(self):
        return "Login" in self.driver.page_source

    def login(self, username, password):
        self.driver.find_element(
            *LoginPageLocators.username).send_keys(username)
        self.driver.find_element(
            *LoginPageLocators.password).send_keys(password)

    def click_login_button(self):
        return self.driver.find_element(*LoginPageLocators.login_button).click()

    def check_error(self):
        return "Epic sadface: Sorry, this user has been locked out." in self.driver.page_source


class InventoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_title(self):
        return 'Swag Labs' in self.driver.title

    def backpack_info(self):
        return self.driver.find_element(*IventoryPageLocators.backpack).click()

    def bikelight_info(self):
        return self.driver.find_element(*IventoryPageLocators.bikelight).click()

    def logout(self):
        self.driver.find_element(*IventoryPageLocators.left_menu).click()
        return self.driver.find_element(*IventoryPageLocators.logout_button).click()

    def add_backpack(self):
        return self.driver.find_element(*IventoryPageLocators.add_backpack).click()

    def check_add_backpack_success(self):
        return self.driver.find_element(*IventoryPageLocators.remove_backpack).text == "Remove"

    def go_to_cart(self):
        return self.driver.find_element(*IventoryPageLocators.cart).click()


class InventoryInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_backpack(self):
        return "Back to products" and "Sauce Labs Backpack" in self.driver.page_source

    def check_bikelight(self):
        return "Back to products" and "Sauce Labs Bike Light" in self.driver.page_source

    def back_to_product(self):
        return self.driver.find_element(
            *InventoryInfoPageLocator.back_to_product).click()


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_in(self):
        return "Your Cart" in self.driver.page_source

    def check_backpack(self):
        return "Backpack" in self.driver.page_source
