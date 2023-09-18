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

from scraper_api import ScraperAPIClient
client = ScraperAPIClient("2d198efa21af1b53905fba1d52541b25")


a = """<ul data-original-position="open-right" class="open-right" style="">
	<li class="imMnMnFirst imLevel" data-link-paths=",/apple-iphone-smartphone-verkaufen-seite-1.html" data-link-hash="-1004153238"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="apple-iphone-smartphone-verkaufen-seite-1.html" class="label" onclick="return x5engine.utils.location('apple-iphone-smartphone-verkaufen-seite-1.html', null, false)">Apple Iphone</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/blackberry-smartphone-verkaufen.html" data-link-hash="-1004156449"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="blackberry-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('blackberry-smartphone-verkaufen.html', null, false)">BlackBerry</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/google-smartphone-verkaufen.html" data-link-hash="-1004153504"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="google-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('google-smartphone-verkaufen.html', null, false)">Google</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/honor-smartphone-verkaufen.html" data-link-hash="-1004154929"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="honor-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('honor-smartphone-verkaufen.html', null, false)">Honor</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/huawei-smartphone-verkaufen.html" data-link-hash="-1004155043"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="huawei-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('huawei-smartphone-verkaufen.html', null, false)">Huawei</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/htc-smartphone-verkaufen.html" data-link-hash="-1004154948"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="htc-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('htc-smartphone-verkaufen.html', null, false)">HTC</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/lg-smartphone-verkaufen.html" data-link-hash="-1004155081"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="lg-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('lg-smartphone-verkaufen.html', null, false)">LG</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/nokia-smartphone-verkaufen.html" data-link-hash="-1004155062"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="nokia-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('nokia-smartphone-verkaufen.html', null, false)">Nokia</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/oneplus-smartphone-verkaufen.html" data-link-hash="-1004154834"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="oneplus-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('oneplus-smartphone-verkaufen.html', null, false)">OnePlus</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/samsung-smartphone-verkaufen.html" data-link-hash="-1004155024"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="samsung-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('samsung-smartphone-verkaufen.html', null, false)">Samsung</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/sony-smartphone-verkaufen.html" data-link-hash="-1004154986"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="sony-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('sony-smartphone-verkaufen.html', null, false)">Sony</a></div></div></li><li class="imMnMnLast imLevel" data-link-paths=",/xiaomi-smartphone-verkaufen.html" data-link-hash="-1004153485"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="xiaomi-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('xiaomi-smartphone-verkaufen.html', null, false)">Xiaomi</a></div></div></li></ul>"""

os.environ['GOOGLEc_APPLICATION_CREDENTIALS'] = 'credentials.json'

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
    sheet_name = "handyverkauf_daily"

    if '/yashin' in os.getcwd():
        filename = os.getcwd()+"/"+sheet_name+".csv"
    else:
        filename = '/home/admin/'+sheet_name+".csv"


    with open(filename,"a") as f:
        writer = csv.writer(f)
        writer.writerow(['scrapped time','brand','link','title','variation','storage','color','condition','functionality','vendor','price','vendor','price','vendor','price','EUR -> HKD','EUR -> AUD'])

    scrapped_time = datetime.datetime.now().strftime("%Y-%m-%d (%H:%M)")

    eur_hkd_rate = requests.post(
        "https://wise.com/gateway/v3/quotes/",
        json={
            "sourceAmount": 100,
            "sourceCurrency": "EUR",
            "targetCurrency": "HKD",
            "preferredPayIn": None,
            "guaranteedTargetAmount": False,
            "type": "REGULAR",
        },
    ).json()['rate']


    eur_aud_rate = requests.post(
        "https://wise.com/gateway/v3/quotes/",
        json={
            "sourceAmount": 100,
            "sourceCurrency": "EUR",
            "targetCurrency": "AUD",
            "preferredPayIn": None,
            "guaranteedTargetAmount": False,
            "type": "REGULAR",
        },
    ).json()['rate']


    brands = ["iphone","samsung","huawei","sony","oneplus","oppo","google","xiaomi","motorola","nokia","lg","realme","blackberry",
              "razer","nothing"]

    # for brand in brands:
    #     # driver.get(f"https://www.handyverkauf.net/?preisvergleich={brand}")
    #     # req = client.get(f"https://www.handyverkauf.net/?preisvergleich={brand}").text
    #     # response = Selector(text=)
    #     links = ['https:'+str(i) for i in Selector(text=client.get(f"https://www.handyverkauf.net/?preisvergleich={brand}").text).xpath('.//a[contains(.,"Verkaufen")]/@href[contains(.,"-")]').extract()]

    links = []
    with open("handerverkauf_input.csv","r") as r:
        reader = csv.reader(r)
        for line in reader:
            if line[0] not in links:
                links.append(line[0])

    for link in list(set(links)):
        id = link.split('h_')[-1]
        response = Selector(text=client.get(link).text)

        title = response.xpath('.//h1[@class="handy_name"]/text()').extract_first()
        try:
            variation = ''.join(response.xpath('.//*[@class="handy_variation"]/text()').extract()).strip()
        except:
            variation = ''
        try:
            storage = variation.split()[0]
        except:
            storage = ''
        try:
            color = variation.split()[-1]
        except:
            color = ''

        mk_id = response.xpath('.//*[@id="inputSuccess1"]/@data-mk').extract_first()

        for optischer in [10,1,2,3,4]:
            for funct in [1,0]:

                try:
                    req = client.get(f"https://www.handyverkauf.net/addons/pausgabe_neu.php?id={id}&w={funct}&z={optischer}&s=0&mode=handy&mk={mk_id}")

                    sel = Selector(text=req.json()['vergleich'].replace('\\',''))

                    datas = sel.xpath('.//*[@style="border-bottom:1px solid #EAEAEA; border-left:1px solid #EAEAEA; border-right:1px solid #EAEAEA;"]').extract()[:3]

                    temp = []
                    for data in datas:
                        sel1 = Selector(text=data)
                        vendor = sel1.xpath('.//a/img/@alt').extract_first()
                        price = sel1.xpath('.//span/a/text()[contains(.,"€")]').extract_first()
                        temp.append(vendor)
                        temp.append(price)

                    temp += [None]*(6-len(temp))

                    if optischer == 10:
                        condition = "Brand New"
                    elif optischer == 1:
                        condition = "Like New"
                    elif optischer == 2:
                        condition = "Very Good"
                    elif optischer == 3:
                        condition = "Good"
                    else:
                        condition = "Acceptable"


                    if funct == 1:
                        functionality = "Fully Functional"
                    else:
                        functionality = "malfunction"


                    with open(filename,"a") as f:
                        writer = csv.writer(f)
                        writer.writerow([datetime.datetime.now().strftime("%Y-%m-%d (%H:%M)"),brand,link,title,variation,storage,color,condition,functionality]+temp+[eur_hkd_rate,eur_aud_rate])
                        print([datetime.datetime.now().strftime("%Y-%m-%d (%H:%M)"),brand,link,title,variation,storage,color,condition,functionality]+temp+[eur_hkd_rate,eur_aud_rate])
                        # print([scrapped_time,brand,link,title,variation,storage,condition,functionality]+temp)

                except:
                    pass
                    # break
                # break
            # break

    uploadtospreadsheet()
