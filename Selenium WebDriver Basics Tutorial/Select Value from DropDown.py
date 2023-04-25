from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://demo.guru99.com/test/newtours/register.php')

# Find and set dropbox
Country = driver.find_element(By.NAME, "country")
dropCountry = Select(Country)

# Select ANTARCTICA
dropCountry.select_by_visible_text("ANTARCTICA")


# Selecting Items in a Multiple SELECT elements
driver.get('http://jsbin.com/osebed/2')
fruits = driver.find_element(By.ID, "fruits")
dropFruits = Select(fruits)
dropFruits.select_by_visible_text("Banana")
dropFruits.select_by_index(1)
