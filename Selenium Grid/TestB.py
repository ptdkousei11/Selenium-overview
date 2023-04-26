from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# java -jar selenium-server-4.9.0.jar standalone

# Declaration and instantiation of objects/variables
driver = webdriver.Remote(command_executor='http://localhost:4444',
                          desired_capabilities={
                              'browserName': 'MicrosoftEdge', 'javascriptEnabled': True})

driver.get('https://demo.guru99.com/test/newtours/')

linkElements = driver.find_elements(
    By.XPATH, "//tbody/tr/td/table/tbody/tr/td//child::a")

linkText = []

for element in linkElements:
    linkText.append(element.text)

# Last 2 link is down so I pop them
linkText.pop(-1)
linkText.pop(-1)

underConsTitle = "Under Construction: Mercury Tours"

for link in linkText:
    driver.find_element(By.LINK_TEXT, link).click()
    if driver.title == underConsTitle:
        print(link, "is under construction.")
    else:
        print(link, "is working.")
    driver.back()

driver.close()
