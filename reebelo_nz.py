import os
import platform

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

"""pip install google-auth==1.28.0
pip install google-api-python-client==2.7.0"""

if platform.system() == "Windows":
    try:
        import undetected_chromedriver
        from parsel import Selector
        from selenium import webdriver
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        import requests
    except ImportError:
        os.system('python -m pip install parsel')
        os.system('python -m pip install selenium==4.9.0')
        os.system('python -m pip install undetected_chromedriver')
        os.system('python -m pip install google-auth==1.28.0')
        os.system('python -m pip install google-api-python-client==2.7.0')
        os.system('python -m pip install requests')

else:
    try:
        import undetected_chromedriver
        from parsel import Selector
        from selenium import webdriver
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        import requests
    except ImportError:
        os.system('python3 -m pip install parsel')
        os.system('python3 -m pip install selenium==4.9.0')
        os.system('python3 -m pip install undetected_chromedriver')
        os.system('python3 -m pip install google-auth==1.28.0')
        os.system('python3 -m pip install google-api-python-client==2.7.0')
        os.system('python3 -m pip install requests')

from selenium import webdriver
import re
import time
from parsel import Selector
import csv
from google.oauth2 import service_account
from googleapiclient.discovery import build
import undetected_chromedriver as uc
import datetime
import requests
from selenium.webdriver.firefox.options import Options
import json


a = """<ul data-original-position="open-right" class="open-right" style="">
	<li class="imMnMnFirst imLevel" data-link-paths=",/apple-iphone-smartphone-verkaufen-seite-1.html" data-link-hash="-1004153238"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="apple-iphone-smartphone-verkaufen-seite-1.html" class="label" onclick="return x5engine.utils.location('apple-iphone-smartphone-verkaufen-seite-1.html', null, false)">Apple Iphone</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/blackberry-smartphone-verkaufen.html" data-link-hash="-1004156449"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="blackberry-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('blackberry-smartphone-verkaufen.html', null, false)">BlackBerry</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/google-smartphone-verkaufen.html" data-link-hash="-1004153504"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="google-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('google-smartphone-verkaufen.html', null, false)">Google</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/honor-smartphone-verkaufen.html" data-link-hash="-1004154929"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="honor-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('honor-smartphone-verkaufen.html', null, false)">Honor</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/huawei-smartphone-verkaufen.html" data-link-hash="-1004155043"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="huawei-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('huawei-smartphone-verkaufen.html', null, false)">Huawei</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/htc-smartphone-verkaufen.html" data-link-hash="-1004154948"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="htc-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('htc-smartphone-verkaufen.html', null, false)">HTC</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/lg-smartphone-verkaufen.html" data-link-hash="-1004155081"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="lg-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('lg-smartphone-verkaufen.html', null, false)">LG</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/nokia-smartphone-verkaufen.html" data-link-hash="-1004155062"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="nokia-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('nokia-smartphone-verkaufen.html', null, false)">Nokia</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/oneplus-smartphone-verkaufen.html" data-link-hash="-1004154834"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="oneplus-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('oneplus-smartphone-verkaufen.html', null, false)">OnePlus</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/samsung-smartphone-verkaufen.html" data-link-hash="-1004155024"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="samsung-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('samsung-smartphone-verkaufen.html', null, false)">Samsung</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/sony-smartphone-verkaufen.html" data-link-hash="-1004154986"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="sony-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('sony-smartphone-verkaufen.html', null, false)">Sony</a></div></div></li><li class="imMnMnLast imLevel" data-link-paths=",/xiaomi-smartphone-verkaufen.html" data-link-hash="-1004153485"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="xiaomi-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('xiaomi-smartphone-verkaufen.html', null, false)">Xiaomi</a></div></div></li></ul>"""

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

def uploadtospreadsheet():
    creds = service_account.Credentials.from_service_account_file('credentials.json')

    # credentials, project = google.auth.default(scopes=['https://www.googleapis.com/auth/spreadsheets'])
    service = build('sheets', 'v4', credentials=creds)

    spreadsheet_id = spreadsheet_url.split('/')[-2]

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)

    request = {
        'range': sheet_name,
        'values': rows,
        'majorDimension': 'ROWS',
    }

    # Execute the request to append the data to the sheet
    response = service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id,
        range=sheet_name,
    ).execute()

    response = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=sheet_name,
        valueInputOption='USER_ENTERED',
        insertDataOption='INSERT_ROWS',
        body=request
    ).execute()

    print(f'{response.get("updates").get("updatedRows")} rows updated.')

if __name__ == '__main__':


    spreadsheet_url = "https://docs.google.com/spreadsheets/d/1KaBHOgUEwVfrUmoMvzsIoH6aIhZdNhlDXquF3lq7NGs/edit#gid=0"
    sheet_name = "reebelo_nz"

    if '/yashin' in os.getcwd():
        filename = os.getcwd()+"/"+sheet_name+".csv"
    else:
        filename = '/home/admin/'+sheet_name+".csv"


    nz_hkd_rate = requests.post("https://wise.com/gateway/v3/quotes/",json={"sourceAmount": 100,"sourceCurrency": "NZD","targetCurrency": "HKD","preferredPayIn": None,"guaranteedTargetAmount": False,"type": "REGULAR",},).json()['rate']
    nz_aud_rate = requests.post("https://wise.com/gateway/v3/quotes/",json={"sourceAmount": 100,"sourceCurrency": "NZD","targetCurrency": "AUD","preferredPayIn": None,"guaranteedTargetAmount": False,"type": "REGULAR",},).json()['rate']
    nz_usd_rate = requests.post("https://wise.com/gateway/v3/quotes/",json={"sourceAmount": 100,"sourceCurrency": "NZD","targetCurrency": "USD","preferredPayIn": None,"guaranteedTargetAmount": False,"type": "REGULAR",},).json()['rate']
    nz_eur_rate = requests.post("https://wise.com/gateway/v3/quotes/",json={"sourceAmount": 100,"sourceCurrency": "NZD","targetCurrency": "EUR","preferredPayIn": None,"guaranteedTargetAmount": False,"type": "REGULAR",},).json()['rate']

    aud_hkd_rate = requests.post("https://wise.com/gateway/v3/quotes/",json={"sourceAmount": 100,"sourceCurrency": "AUD","targetCurrency": "HKD","preferredPayIn": None,"guaranteedTargetAmount": False,"type": "REGULAR",},).json()['rate']
    aud_usd_rate = requests.post("https://wise.com/gateway/v3/quotes/",json={"sourceAmount": 100,"sourceCurrency": "AUD","targetCurrency": "USD","preferredPayIn": None,"guaranteedTargetAmount": False,"type": "REGULAR",},).json()['rate']
    aud_eur_rate = requests.post("https://wise.com/gateway/v3/quotes/",json={"sourceAmount": 100,"sourceCurrency": "AUD","targetCurrency": "EUR","preferredPayIn": None,"guaranteedTargetAmount": False,"type": "REGULAR",},).json()['rate']


    with open(filename,"a") as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp','link','title','sold','brand','vendor','ram','sku','color','condition','storage','connectivity','simslot','price',
                         'NZD -> HKD','NZD -> AUD','NZD -> USD','NZD -> EUR','AUD -> HKD','AUD -> USD','AUD -> EUR'])


    alreadyscrapped = []
    firefox_options = Options()
    firefox_options.headless = True if not '/yashin' in os.getcwd() else False
    driver = webdriver.Firefox(options=firefox_options)

    driver.get("https://reebelo.co.nz/collections/smartphones?sort=latest-release")
    links = Selector(text=driver.page_source).xpath('.//*[@class="flex h-full w-full flex-col items-center justify-start text-gray-700"]/@href').extract()
    for link in links:
        driver.get("https://reebelo.co.nz"+link)

        sel = Selector(text=driver.page_source)
        try:
            sold = sel.xpath('.//*[@class="mr-2 text-xs"][contains(.,"Sold")]/text()').extract_first().replace('Sold','').replace('+','')
        except:
            sold = ''

        try:
            jsondata = json.loads(sel.xpath('.//*[@id="__NEXT_DATA__"]/text()').extract_first())

            for data in jsondata['props']['pageProps']['offers']:
                title = sel.xpath('.//h1[@id="e2e-product-name"]/text()').extract_first()
                brand = data['brand']
                vendor = data['vendor']
                try:
                    ram = data['ram']
                except:
                    ram = ''

                sku = data['sku']
                try:
                    color = data['color']
                except:
                    color = ''
                try:
                    condition = data['tags'][-1].replace('Condition_','')
                except:
                    condition = ''
                try:
                    storage = data['storage']
                except:
                    storage = ''
                try:
                    connectivity = data['connectivity']
                except:
                    connectivity = ''
                try:
                    simslot = data['simSlot']
                except:
                    simslot = ''
                try:
                    price = data['price']
                except:
                    price = ''

                if ["https://reebelo.co.nz"+link,title,brand,vendor,ram,sku,color,condition,storage,connectivity,simslot,price] not in alreadyscrapped:
                    alreadyscrapped.append(["https://reebelo.co.nz"+link,title,brand,vendor,ram,sku,color,condition,storage,connectivity,simslot,price])
                    with open(filename,"a") as f:
                        writer = csv.writer(f)
                        writer.writerow([datetime.datetime.now().strftime("%Y-%m-%d (%H:%M)"),"https://reebelo.co.nz"+link,title,sold,brand,vendor,ram,sku,color,condition,storage,connectivity,simslot,price,
                                         nz_hkd_rate,nz_aud_rate,nz_usd_rate,nz_eur_rate,aud_hkd_rate,aud_usd_rate,aud_eur_rate])
                        print([datetime.datetime.now().strftime("%Y-%m-%d (%H:%M)"),"https://reebelo.co.nz"+link,title,sold,brand,vendor,ram,sku,color,condition,storage,connectivity,simslot,price,
                               nz_hkd_rate,nz_aud_rate,nz_usd_rate,nz_eur_rate,aud_hkd_rate,aud_usd_rate,aud_eur_rate])

                else:
                    print("Exists...")

        except:
            pass

    driver.close()

    uploadtospreadsheet()