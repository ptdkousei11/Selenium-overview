from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://demo.guru99.com/test/newtours/')

print(driver.find_element(By.PARTIAL_LINK_TEXT, "egis").text)

print(driver.find_element(By.PARTIAL_LINK_TEXT, "EGIS").text)

driver.close()
