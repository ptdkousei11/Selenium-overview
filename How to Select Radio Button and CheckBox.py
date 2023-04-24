from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://demo.guru99.com/test/radio.html')

# Find radio button
radio1 = driver.find_element(By.ID, "vfb-7-1")
radio2 = driver.find_element(By.ID, "vfb-7-2")

# Radio Button1 is selected
radio1.click()
print("Radio Button Option 1 Selected")

# Radio Button2 is selected
radio2.click()
print("Radio Button Option 2 Selected")

# Selecting CheckBox
option1 = driver.find_element(By.ID, "vfb-6-0")

# This will Toggle the Check box
option1.click()

# Check whether the Check box is toggled on
if (option1.is_selected()):
    print("Checkbox is Toggled On")
else:
    print("Checkbox is Toggled Off")
