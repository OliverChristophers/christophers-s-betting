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
  
    
    list_keys = ['Total Goals Over/Under', 'Time of First Goal', 'Correct Score - 1st Half']

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


listgames =['https://www.oddschecker.com/football/english/fa-cup/wigan-v-luton-town/winner', 'https://www.oddschecker.com/football/english/fa-cup/forest-green-v-birmingham/winner', 'https://www.oddschecker.com/football/english/fa-cup/swansea-v-bristol-city/winner', 'https://www.oddschecker.com/football/english/fa-cup/accrington-v-boreham-wood/winner', 'https://www.oddschecker.com/football/english/fa-cup/wolves-v-liverpool/winner', 'https://www.oddschecker.com/football/english/fa-cup/west-brom-v-chesterfield/winner', 'https://www.oddschecker.com/football/english/non-league/national-league/solihull-moors-v-aldershot/winner', 'https://www.oddschecker.com/football/english/non-league/national-league/barnet-v-yeovil/winner', 'https://www.oddschecker.com/football/english/non-league/national-league/altrincham-v-maidenhead-utd/winner', 'https://www.oddschecker.com/football/english/non-league/national-league/wealdstone-v-oldham/winner', 'https://www.oddschecker.com/football/english/non-league/national-league/dag-red-v-eastleigh/winner', 'https://www.oddschecker.com/football/english/non-league/national-league/torquay-v-bromley/winner', 'https://www.oddschecker.com/football/spain/copa-del-rey/real-sociedad-v-mallorca/winner', 'https://www.oddschecker.com/football/spain/copa-del-rey/cd-alaves-v-sevilla/winner', 'https://www.oddschecker.com/football/italy/coppa-italia/napoli-v-cremonese/winner', 'https://www.oddschecker.com/football/english/non-league/national-league-north/brackley-town-v-kings-lynn/winner', 'https://www.oddschecker.com/football/english/non-league/national-league-north/farsley-celtic-fc-v-leamington/winner', 'https://www.oddschecker.com/football/english/non-league/national-league-north/afc-fylde-v-buxton/winner', 'https://www.oddschecker.com/football/english/non-league/national-league-north/southport-v-boston-utd/winner', 'https://www.oddschecker.com/football/english/non-league/national-league-north/peterborough-sports-v-gloucester-city/winner', 'https://www.oddschecker.com/football/english/non-league/national-league-north/afc-telford-united-v-kettering-town/winner', 'https://www.oddschecker.com/football/english/non-league/national-league-south/bath-v-dulwich/winner', 'https://www.oddschecker.com/football/english/non-league/national-league-south/hungerford-town-v-st-albans-city/winner', 'https://www.oddschecker.com/football/english/non-league/national-league-south/ebbsfleet-united-v-chelmsford/winner', 'https://www.oddschecker.com/football/english/non-league/national-league-south/farnborough-v-slough/winner', 'https://www.oddschecker.com/football/english/non-league/national-league-south/chippenham-v-welling-utd/winner', 'https://www.oddschecker.com/football/english/non-league/national-league-south/hampton-v-cheshunt/winner', 'https://www.oddschecker.com/football/english/non-league/fa-trophy/harrow-borough-v-fc-halifax-town/winner', 'https://www.oddschecker.com/football/english/non-league/fa-trophy/torquay-united-v-taunton-town/winner', 'https://www.oddschecker.com/football/english/non-league/fa-trophy/banbury-united-v-coalville-town/winner', 'https://www.oddschecker.com/antalyaspor-v-kayserispor/winner', 'https://www.oddschecker.com/alanyaspor-v-galatasaray/winner', 'https://www.oddschecker.com/football/belgium/jupiler-pro-league/oh-leuven-v-eupen/winner', 'https://www.oddschecker.com/football/belgium/jupiler-pro-league/standard-liege-v-kv-mechelen/winner', 'https://www.oddschecker.com/football/belgium/jupiler-pro-league/westerlo-v-genk/winner', 'https://www.oddschecker.com/football/friendlies/real-murcia-v-sc-paderborn/winner', 'https://www.oddschecker.com/football/friendlies/mfk-zemplin-michalovce-v-kazincbarcika-bsc/winner', 'https://www.oddschecker.com/football/friendlies/st-polten-v-haladas/winner', 'https://www.oddschecker.com/football/friendlies/zalaegerszegi-v-mfk-ruzomberok/winner', 'https://www.oddschecker.com/football/friendlies/honved-v-fk-javor-ivanjica/winner', 'https://www.oddschecker.com/football/friendlies/1.sk-prostejov-v-fk-dukla-banska-bystrica/winner', 'https://www.oddschecker.com/football/friendlies/sv-sandhausen-v-fc-trinity-zlin/winner', 'https://www.oddschecker.com/football/friendlies/levski-sofia-v-al-kuwait/winner', 'https://www.oddschecker.com/football/friendlies/lask-linz-v-ksv-1919/winner', 'https://www.oddschecker.com/football/friendlies/sc-austria-lustenau-v-sc-bruhl/winner', 'https://www.oddschecker.com/football/friendlies/sg-aumund-vegesack-v-bsv-schwarz-weiss-rehden/winner', 'https://www.oddschecker.com/football/friendlies/penarol-v-san-lorenzo/winner']
while True:
    for i in listgames:

        getOdds(i)

    
    time.sleep(600)