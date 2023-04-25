from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://demo.guru99.com/test/login.html')

# Find email box and pass box
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "passwd")

# Set
email.send_keys("abcd@gmail.com")
password.send_keys("abcdefghlkjl")
print("Text Field Set")

# Clear
email.clear()
password.clear()
print("Text Field Cleared")

# Find sign in button
login_button = driver.find_element(By.ID, "SubmitLogin")

# et and click
email.send_keys("abcd@gmail.com")
password.send_keys("abcdefghlkjl")
login_button.click()
print("Login Done with Click")
