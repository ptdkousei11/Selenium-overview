from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('http://demo.guru99.com/test/newtours/')

link_Home = driver.find_element(By.LINK_TEXT, "Home")
td_Home = driver.find_element(
    By.XPATH, "//table[@bordercolor='#000000']/tbody/tr/td[@width='20']")

bgColor = td_Home.value_of_css_property("background-color")
print("Before hover:", bgColor)

action = ActionChains(driver)
action.move_to_element(link_Home)
action.perform()

bgColor = td_Home.value_of_css_property("background-color")
print("After hover:", bgColor)

driver.close()
