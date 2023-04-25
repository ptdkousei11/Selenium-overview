from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Using X-Path to Locate Web Table Elements
# Example: Get all the values of a Dynamic Table

# Declaration and instantiation of objects/variables
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(
    executable_path=r'C:\Program Files (x86)\geckodriver.exe',
    options=options)

driver.get('https://demo.guru99.com/test/table.html')
driver.implicitly_wait(5)

# Locate the table
table = driver.find_element(
    By.XPATH, "//table[@cellspacing = '1']/tbody")

# Locate rows of table
rows = table.find_elements(By.TAG_NAME, "tr")

# Set rows count
rows_count = 0

# Loop will execute till the last row of table.
for row in rows:
    # To locate columns(cells) of that specific row.
    columns_rows = row.find_elements(By.TAG_NAME, "td")
    # To calculate no of columns (cells). In that specific row.
    columns_count = len(columns_rows)
    print("Number of cells In Row", rows_count, "are", columns_count)
    # Loop will execute till the last cell of that specific row.
    for column in columns_rows:
        # To retrieve text from that specific cell.
        celtext = column.text
        print("Cell Value of row number", rows_count,
              "and column number", column.text, "is", celtext)

    rows_count = rows_count + 1

driver.close()
