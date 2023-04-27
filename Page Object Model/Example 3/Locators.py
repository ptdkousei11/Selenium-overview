from selenium.webdriver.common.by import By


class LoginPageLocators():
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error = (By.CLASS_NAME, "error-message-container error")


class IventoryPageLocators():
    backpack = (By.XPATH, "//a[@id='item_4_title_link']/div")
    bikelight = (By.XPATH, "//a[@id='item_0_title_link']/div")
    tshirt = (By.XPATH, "//a[@id='item_1_title_link']/div")
    jacket = (By.XPATH, "//a[@id='item_5_title_link']/div")
    onesie = (By.XPATH, "//a[@id='item_2_title_link']/div")
    tshirt_red = (By.XPATH, "//a[@id='item_3_title_link']/div")
    logout_button = (By.XPATH, "//*[@id='logout_sidebar_link']")
    left_menu = (By.ID, "react-burger-menu-btn")
    add_backpack = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    remove_backpack = (By.XPATH, "//*[@id='remove-sauce-labs-backpack']")
    cart = (By.XPATH, "//*[@id='shopping_cart_container']/a")


class InventoryInfoPageLocator():
    back_to_product = (By.ID, "back-to-products")
