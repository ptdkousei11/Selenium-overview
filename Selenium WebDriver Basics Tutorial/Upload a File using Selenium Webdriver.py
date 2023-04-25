from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://demo.guru99.com/test/upload/')

uploadElement = driver.find_element(By.ID, "uploadfile_0")

# Enter the file path onto the file-selection input field
uploadElement.send_keys("D:\ptdat-batch40\Selenium-overview\README.md")

# Check the "I accept the terms of service" check box
driver.find_element(By.ID, "terms").click()

# Click the "UploadFile" button
driver.find_element(By.ID, "submitbutton").click()
