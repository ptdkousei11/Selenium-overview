from selenium.webdriver.common.by import By


class LoginPageLocators():
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error = (By.CLASS_NAME, "error-message-container error")
