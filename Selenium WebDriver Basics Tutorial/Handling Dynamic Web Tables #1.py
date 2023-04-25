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

# No. of Columns
columns = driver.find_elements(
    By.XPATH, "//div[@id = 'leftcontainer']/table/thead/tr/th")

print("No of columns are:", len(columns))

# No. of Rows
rows = driver.find_elements(
    By.XPATH, "//div[@id = 'leftcontainer']/table/tbody/tr/td")

print("No of rows are:", len(rows))

driver.close()
