#get bet site

#find when teams playing

#start new terminal

#add model


import undetected_chromedriver as uc
import time
from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime
import json
import xlsxwriter
from bs4 import BeautifulSoup as bs
import os


 
    
 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
options = uc.ChromeOptions()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))
options.add_argument('--headless')
driver = uc.Chrome(options=options)


def getLive():
    driver.get('https://www.oddschecker.com/football/accumulator')

    time.sleep(2)




    try:
        button1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/h2/span[2]')
        driver.execute_script("arguments[0].click();", button1)
    except:
        pass
    try:
        btn = driver.find_element(By.XPATH, '/html/body/main/div/div[5]/div/div/button[1]')
        driver.execute_script("arguments[0].click();", btn)
    except:
        pass
    try:
        btn1 = driver.find_element(By.XPATH, '/html/body/main/div/div[6]/div/div[2]/div[2]')
        driver.execute_script("arguments[0].click();", btn1)
    except:
        pass



    element = driver.find_elements(By.CLASS_NAME, 'arrow_a1f1ukjc')

    for state in element:
        xpanded = state.get_attribute("aria-expanded")

        if xpanded == 'false':
            driver.execute_script("arguments[0].click();", state) 
        
    time.sleep(3)
    new_list = []

    start_time = driver.find_elements(By.CLASS_NAME, 'StartTimeText_s1cr9nsi')
    for i in start_time:
        currentDateAndTime = datetime.now()
        currentTime = currentDateAndTime.strftime("%H:%M")
        #currentDateAndTime.strftime("%H:%M")
        new = i.text.split(':')
        newnew = currentTime.split(':')
        
        
        check = 60 - int(newnew[-1])


        if (int(new[0]) + 1) - int(newnew[0]) == 1:
            if int(new[-1]) == 0 and int(newnew[-1]) >= 41:
                new_list.append(i.get_attribute('href'))
            
        elif check <= 5:
            if int(new[-1]) == 15:
                new_list.append(i.get_attribute('href'))


        if (int(new[0]) + 1) - int(newnew[0]) == 0:
            if int(new[-1]) == 0:
                pass

            elif int(newnew[-1]) < int(new[-1]):
                if int(new[-1]) - int(newnew[-1]) <= 30:
                    new_list.append(i.get_attribute('href'))
        
    return new_list

print(getLive())