from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://demo.guru99.com/test/delete_customer.php')

driver.find_element(By.NAME, "cusid").send_keys("53920")
driver.find_element(By.NAME, "submit").submit()

alert = driver.switch_to.alert

alertMsg = alert.text

print(alertMsg)

time.sleep(3)

alert.accept()
