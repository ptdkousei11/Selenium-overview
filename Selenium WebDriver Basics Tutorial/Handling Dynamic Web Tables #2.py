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

driver.get('https://demo.guru99.com/test/web-table-element.php')

baseTable = driver.find_element(By.TAG_NAME, "table")

tableRow = baseTable.find_element(
    By.XPATH, "//div[@id='leftcontainer']/table/tbody/tr[3]")

print("Third row of table:", tableRow.text)

cell = tableRow.find_element(
    By.XPATH, "//div[@id='leftcontainer']/table/tbody/tr[3]/td[2]")

print("Cell value is:", cell.text)

driver.close()
