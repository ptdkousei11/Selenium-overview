from element import BasePageElement
from locators import MainPageLocators


class SearchUserElement(BasePageElement):
    locator = 'user-name'


class SearchPasswordElement(BasePageElement):
    locator = 'password'


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here."""

    # Declares a variable that will contain the retrieved text
    search_user_element = SearchUserElement()
    search_password_element = SearchPasswordElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Swag Labs" in self.driver.title

    def click_login_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        return "Products" in self.driver.page_source
