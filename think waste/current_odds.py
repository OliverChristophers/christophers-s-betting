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
import sys


 
    
 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
options = uc.ChromeOptions()
#options.add_argument('--headless')
driver = uc.Chrome(options=options)



def getCurr(url):

    print(url)
    driver.get(url)
    time.sleep(6)
    
    
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
    
    list_keys = ['Total Goals Over/Under']
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


        
        exex = ['1.5', '2.5', '3.5', '4.5']


        '''    firms = []
        firmname = []
        for oi in range(40):

            bookmaker = driver.find_elements(By.XPATH, f'//*[@id="scrollable-container-3547971778"]/div[{oi}]/button')
        
            for ui in bookmaker:
                firms.append(ui.text)
                firmname.append(ui.get_attribute("data-bk"))

        print(firms)
        print(firmname)'''

        texts = []

        for i in text:
            texts.append(i.text)

        
        texes = []
        #firms = ['bet365', 'skybet','paddypower', 'william hill', '888sport', 'betfair', 'betvictor', 'coral', 'unibet', 'spreadEX', 'betfred', 'sbk', 'boylesport', '10bet', 'betuk', 'sporting index', 'livescore bet', 'quinnbet', 'betway', 'ladbrokes', 'midnite', 'parimatch', 'vbet']
        for u in texts:
            free = u.split('\n')
            for t in exex:
                if free[0] == t:


                    texes.append(free)

                
                else:
                    pass
        
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
            f.write(f'\n{ret[-1]}, {currentTime}\n{x}, {texes}')


       


    with open(os.path.realpath(rf'{ret[-1]}.txt'), 'a') as f:
        f.write(f'\n')


list_games = ['https://www.oddschecker.com/football/france/coupe-de-france/brest-v-lens/winner', 'https://www.oddschecker.com/football/italy/serie-a/juventus-v-atalanta/winner', 'https://www.oddschecker.com/football/spain/la-liga-primera/athletic-bilbao-v-real-madrid/winner', 'https://www.oddschecker.com/football/belgium/jupiler-pro-league/sint-truidense-v-gent/winner']

while True:
    
    start = time.time()
    getCurr(sys.argv[1])
    end = time.time()
    taken = end - start
    if taken < 60:
        time.sleep(60 - taken)






['bet365', 'skybet','paddypower', 'william hill', '888sport', 'betfair', 'betvictor', 'coral', 'unibet', 'spreadEX', 'betfred', 'sbk', 'boylesport', '10bet', 'betuk', 'sporting index', 'livescore bet', 'quinnbet', 'betway', 'ladbrokes', 'midnite', 'parimatch', 'vbet']
['B3', 'SK', 'PP', 'WH', 'EE', 'FB', 'VC', 'CE', 'UN', 'SX', 'FR', 'RK', 'BY', 'OE', 'DP', 'SI', 'LS', 'QN', 'WA', 'LD', 'N4', 'RM', 'VT']



'''bestOddsStyles_b1n2p0rl oddShortening_o1ini8o6 betTooltip_b1ufcx63 OddsCellDesktop_obvpjra OddsCellBtn_o5t2ais
bestOddsStyles_b1n2p0rl oddDrifting_o14s2hvj betTooltip_b1ufcx63 OddsCellDesktop_obvpjra OddsCellBtn_o5t2ais
bestOddsStyles_b1n2p0rl oddStable_o1ggra3k betTooltip_b1ufcx63 OddsCellDesktop_obvpjra OddsCellBtn_o5t2ais'''