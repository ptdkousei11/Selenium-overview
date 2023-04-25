from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://www.guru99.com/selenium-tutorial.html')

driver.find_element(By.XPATH, "//a[@href='https://www.guru99.com/']").click()

if (driver.title == "Meet Guru99 – Free Training Tutorials & Video for IT Courses"):
    print("We are back at GURU99's homepage!")
else:
    print("We are NOT in GURU99's homepage!")
