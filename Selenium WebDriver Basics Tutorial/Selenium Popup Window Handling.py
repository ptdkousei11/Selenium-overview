from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://demo.guru99.com/popup.php')

main_page = driver.current_window_handle

driver.find_element(By.XPATH, "//*[contains(@href,'popup.php')]").click()

sleep(5)

for handle in driver.window_handles:
    if handle != main_page:
        popup = handle

driver.switch_to.window(popup)

driver.find_element(By.NAME, "emailid").send_keys("gaurav.3n@gmail.com")

driver.find_element(By.NAME, "btnLogin").click()

driver.close()

driver.switch_to.window(main_page)

sleep(3)

driver.close()
