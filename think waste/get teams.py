import undetected_chromedriver as uc
import time
from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime
import json
import xlsxwriter



from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = uc.ChromeOptions()
options.add_argument('--headless')
driver = uc.Chrome(options=options)



def getTeams():
    driver.get('https://www.oddschecker.com/football/accumulator')
    time.sleep(2)

    element = driver.find_elements(By.CLASS_NAME, 'arrow_a1f1ukjc')

    for state in element:
        xpanded = state.get_attribute("aria-expanded")

        if xpanded == 'false':
            driver.execute_script("arguments[0].click();", state) 
        
    time.sleep(5)

    team = driver.find_elements(By.CLASS_NAME, 'BetWrapper_bn6y2jt')
    new_list = []

    for i in team:
        new_list.append(i.get_attribute('href'))

    
    
    return new_list


print(getTeams())