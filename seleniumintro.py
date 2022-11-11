from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    #options = Options()
    #options.add_argument(("--incognito", "--start-maximized", "--headless")
    #options.add_argument("download.default_directory=")  #if you are downloading somthing we need to specify where is going
    driver = webdriver.Chrome()
    driver.get("https://fgcuathletics.com/sports/womens-soccer/stats/2022")
    assert "Page not found" not in driver.page_source

    table_rows = []
    #elem = driver.find_element(By.CLASS_NAME, "sidearm-table") #was change to x path in net line
    table_data = driver.find_elements(By.XPATH, "//table[1]//th")
    """headers = []
    for header in table_data[0:3]:
        headers.append(header.text)"""
    table_rows.append([h.text for h in table_data[0:3]])



    table_data = driver.find_elements(By.XPATH, "//table[1]/tbody/tr")
    for row in table_data:
        if row.text:
            cur_row = row.text.split(" ")
            if len(cur_row) != 1:
                table_rows.append(cur_row)

    for i, row in enumerate(table_rows):
        print(f"Row {i} is: {row}")

    driver.close()






"""# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = webdriver.Edge()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/"""


