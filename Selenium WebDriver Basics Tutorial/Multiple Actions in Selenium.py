from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://www.saucedemo.com/')

username = driver.find_element(By.ID, "user-name")

action = ActionChains(driver)

action.move_to_element(username)
action.click()
action.key_down(Keys.SHIFT, username)
action.send_keys('hello')
action.key_up(Keys.SHIFT, username)
action.double_click(username)
action.context_click()
action.perform()
