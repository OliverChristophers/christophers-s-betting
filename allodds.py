import undetected_chromedriver as uc
import time
from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime
import json
import xlsxwriter
from bs4 import BeautifulSoup as bs
import sys


 
reee  = datetime.now()

 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
options = uc.ChromeOptions()
#options.add_argument('--headless')
driver = uc.Chrome(options=options)



def getCurr(url):

    print(url)
    driver.get(url)
    time.sleep(4)
    
    
    button = driver.find_element(By.XPATH, '/html/body/main/div/div[4]/div/section/div[1]/div/div/div[2]')
    driver.execute_script("arguments[0].click();", button)
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
        print('no')
        pass

    list_keys = ['Time Of First Goal', 'Win Market', 'Half Time/Full Time', 'Asian Handicap','cleen sheet', 'Total Goals Exact', 'Total Goals Over/Under', 'Both Teams To Score', 'To Score 2 Or More Goals', 'Score/Win Double', 'Highest Scoring Half', 'Total Corners - 1st Half', 'Team To Score', 'Both Teams To Score In 2nd Half', 'Both Teams To Score And Over/Under 2 5', 'Total Away Corners', 'To Score A Penalty', 'To Win From Behind', 'To Win Both Halves', 'Correct Score', 'Match Result And Both Teams To Score', 'Correct Score - 1st Half', 'Total Corners', 'To Win To Nil', 'Match Result and Over/Under 3 5', 'Match Result and Over/Under 4 5', 'Goal In Both Halves', 'total home corners', 'to score 5+ goals', 'to score 4+ goals', 'most corners', 'to qualify', 'handicaps', 'half time', 'winning margin', 'team to score first', 'double chance', 'both teams to score in 1st half', 'to score in both halves', 'total goals - 1st half', 'to win either half', 'first corner', 'corner handicap', 'most corners', 'total cards']

    time.sleep(2)

    for x in list_keys:
        input = driver.find_element(By.XPATH, '/html/body/main/div/div[4]/div/section/section/div[1]/div/div/div[1]/input')
        input.send_keys(Keys.CONTROL, 'a')
        input.send_keys(Keys.DELETE)
        input.send_keys(x)

        try:
            element = driver.find_element(By.XPATH, '/html/body/main/div/div[4]/div/section/section/div[1]/div/div/div[2]/div/div[1]')
            driver.execute_script("arguments[0].click();", element)

            time.sleep(3)
        
        except:
            continue

        try:
            show_more = driver.find_element(By.XPATH, '/html/body/main/div/div[4]/div/section/section/article/section[1]/div/div/div/div[9]/span')
            driver.execute_script("arguments[0].click();", show_more)
            time.sleep(3)
        
        except:
            pass
        

        try:
            text = driver.find_elements(By.CLASS_NAME, 'MarketExpanderBetWrapper_maljog0')

        except:
            continue


    

        texts = []

        for i in text:
            texts.append(i.text)

        
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


        with open(os.path.realpath(rf'{ret[-1]}.txt'), 'a') as f:
            f.write(f'\n{x}, {texes}')


       


    with open(os.path.realpath(rf'{ret[-1]}.txt'), 'a') as f:
        f.write(f'\n{ret[-1]} {currentTime}\n\n')


p = 0
while True:
    p += 1
    if p >= 40:
        break
    start = time.time()
    getCurr(sys.argv[1])
    end = time.time()
    taken = end - start
    if taken < 60:
        time.sleep(60 - taken)
    




