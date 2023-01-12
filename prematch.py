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





def getOdds(url):
    with open(os.path.realpath(rf'prematch data.txt'), 'a') as f:
            f.write(f'\n{url}')
    print(url)
    driver.get(url)
    time.sleep(2)
    
    button = driver.find_element(By.XPATH, '/html/body/main/div/div[4]/div/section/div[1]/div/div/div[2]')

    try:
        button1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/h2/span[2]')
        driver.execute_script("arguments[0].click();", button1)
    except:
        pass

    driver.execute_script("arguments[0].click();", button)
  
    
    list_keys = ['Total Goals Over/Under', 'Time of First Goal']

    for x in list_keys:
        input = driver.find_element(By.XPATH, '/html/body/main/div/div[4]/div/section/section/div[1]/div/div/div[1]/input')
        input.send_keys(Keys.CONTROL, 'a')
        input.send_keys(Keys.DELETE)
        input.send_keys(x)

        try:
            element = driver.find_element(By.XPATH, '/html/body/main/div/div[4]/div/section/section/div[1]/div/div/div[2]/div/div[1]')
            driver.execute_script("arguments[0].click();", element)

            time.sleep(2)
        
        except:
            continue

        try:
            show_more = driver.find_element(By.XPATH, '/html/body/main/div/div[4]/div/section/section/article/section[1]/div/div/div/div[9]/span')
            driver.execute_script("arguments[0].click();", show_more)
            time.sleep(2)
        
        except:
            pass
        

        try:
            text = driver.find_elements(By.CLASS_NAME, 'MarketExpanderBetWrapper_maljog0')

        except:
            continue

        texts = []
        for u in text:
            texts.append(u.text)

        texes = []
        #firms = ['bet365', 'skybet','paddypower', 'william hill', '888sport', 'betfair', 'betvictor', 'coral', 'unibet', 'spreadEX', 'betfred', 'sbk', 'boylesport', '10bet', 'betuk', 'sporting index', 'livescore bet', 'quinnbet', 'betway', 'ladbrokes', 'midnite', 'parimatch', 'vbet']
        
        
        for u in texts:
            free = u.split('\n')

            texes.append(free)
        

        
        for i in texes:
            ope = 0
            for t in i:
                ope += 1
                if ope == 2:
                    w = t.split('/')
                    try:
                        i[1] = str(round(int(w[0])/int(w[1]) + 1,3))
                    except:
                        pass

        re = url.split('/winner')

        re.remove('')

        ret = re[0].split('/')

        currentDateAndTime = datetime.now()
        currentTime = currentDateAndTime.strftime("%H:%M:%S")


        with open(os.path.realpath(rf'prematch data.txt'), 'a') as f:
            f.truncate()
            f.write(f'\n{x}, {texes}')


    with open(os.path.realpath(rf'prematch data.txt'), 'a') as f:
            f.write(f'{currentTime}, {ret[-1]} \n')


listgames = ['https://www.oddschecker.com/football/english/premier-league/arsenal-v-newcastle/winner', 'https://www.oddschecker.com/football/english/premier-league/everton-v-brighton/winner', 'https://www.oddschecker.com/football/english/premier-league/leicester-v-fulham/winner', 'https://www.oddschecker.com/football/english/premier-league/man-utd-v-bournemouth/winner']
while True:
    for i in listgames:

        getOdds(i)

    
    time.sleep(600)