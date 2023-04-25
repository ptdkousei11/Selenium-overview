from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://demo.guru99.com/test/accessing-nested-table.html')

innerText = driver.find_element(
    By.XPATH, "//table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]")

print(innerText.text)

driver.close()
