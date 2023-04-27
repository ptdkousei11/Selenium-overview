from Locators import LoginPageLocators
from PageBase import PageBase


class LoginPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.driver.find_element(
            *LoginPageLocators.username).send_keys(username)
        self.driver.find_element(
            *LoginPageLocators.password).send_keys(password)

    def click_login_button(self):
        return self.driver.find_element(*LoginPageLocators.login_button).click()

    def check_error(self):
        return "Epic sadface: Sorry, this user has been locked out." in self.driver.page_source


class InventoryPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)

    def check_title(self):
        return 'Swag Labs' in self.driver.title
