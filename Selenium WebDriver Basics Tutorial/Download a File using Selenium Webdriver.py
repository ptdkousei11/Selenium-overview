from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://www.browserstack.com/test-on-the-right-mobile-devices')

cookie = driver.find_element(
    By.XPATH, "//button[@id = 'accept-cookie-notification']")

cookie.click()

downloadcsv = driver.find_element(By.CSS_SELECTOR, ".icon-csv")

downloadcsv.click()
