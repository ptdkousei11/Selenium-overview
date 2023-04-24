from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://demo.guru99.com/test/ajax.html')

# Find the radio button for “No” using its ID and click on it
driver.find_element(By.ID, "yes").click()
driver.find_element(By.ID, "no").click()

# Click on Check Button
driver.find_element(By.ID, "buttoncheck").click()
