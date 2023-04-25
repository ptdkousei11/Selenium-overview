from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Using X-Path to Locate Web Table Elements
# Example: Fetch number of rows and columns from Dynamic WebTable

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://demo.guru99.com/test/newtours/')

linkElements = driver.find_elements(
    By.XPATH, "//tbody/tr/td/table/tbody/tr/td//child::a")

linkText = []

for element in linkElements:
    linkText.append(element.text)

# Last 2 link is down so I pop them
linkText.pop(-1)
linkText.pop(-1)

underConsTitle = "Under Construction: Mercury Tours"

for link in linkText:
    driver.find_element(By.LINK_TEXT, link).click()
    if driver.title == underConsTitle:
        print(link, "is under construction.")
    else:
        print(link, "is working.")
    driver.back()

driver.close()
