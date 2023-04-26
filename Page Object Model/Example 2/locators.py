from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    USER = (By.ID, 'user-name')
    PASS = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass
