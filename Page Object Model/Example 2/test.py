import unittest
from selenium import webdriver
import page

# java -jar selenium-server-4.9.0.jar hub
# java -jar selenium-server-4.9.0.jar node


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://localhost:4444',
                                       desired_capabilities={
                                           'browserName': 'MicrosoftEdge',
                                           'javascriptEnabled': True})
        self.driver.get("https://www.saucedemo.com/")

    def test_search_in_python_org(self):

        # Load the main page. In this case the home page of "https://www.saucedemo.com/".
        main_page = page.MainPage(self.driver)

        # Checks if the word "Swag Labs" is in title
        self.assertTrue(main_page.is_title_matches(),
                        "Title doesn't match.")

        # Sets username and password
        main_page.search_user_element = "standard_user"
        main_page.search_password_element = "secret_sauce"
        main_page.click_login_button()

        search_results_page = page.SearchResultsPage(self.driver)

        # Verifies that login success
        self.assertTrue(search_results_page.is_results_found(),
                        "Error.")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
