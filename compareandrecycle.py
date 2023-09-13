import os
import platform

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

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

a = """<div class="brand-selector-wrap"><span class="brand-box  active"><img alt="Any" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fany.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fany.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fany.svg&amp;w=128&amp;q=75"><span class="selected-icon"></span></span><span class="brand-box "><img alt="Samsung" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fsamsung.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fsamsung.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fsamsung.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="Huawei" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fhuawei.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fhuawei.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fhuawei.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="Apple" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fapple.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fapple.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fapple.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="Sony" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fsony.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fsony.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fsony.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="Oppo" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Foppo.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Foppo.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Foppo.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="OnePlus" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Foneplus.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Foneplus.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Foneplus.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="Google" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fgoogle.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fgoogle.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fgoogle.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="Xiaomi" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fxiaomi.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fxiaomi.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fxiaomi.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="Motorola" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fmotorola.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fmotorola.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fmotorola.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="Honor" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fhonor-logo.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fhonor-logo.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fhonor-logo.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="Nokia" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fnokia.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fnokia.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fnokia.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="BlackBerry" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fblackberry.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fblackberry.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fblackberry.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="LG" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Flg.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Flg.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Flg.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="RealMe" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Frealme.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Frealme.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Frealme.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="Razer" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Frazer.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Frazer.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Frazer.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="HTC" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fhtc.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fhtc.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fhtc.svg&amp;w=128&amp;q=75"></span><span class="brand-box "><img alt="Nothing" loading="lazy" width="57" height="43" decoding="async" data-nimg="1" style="color: transparent;" srcset="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fnothing.svg&amp;w=64&amp;q=75 1x, /_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fnothing.svg&amp;w=128&amp;q=75 2x" src="/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Fprice-snagger-cdn%2Fmanufacturer%2Fnothing.svg&amp;w=128&amp;q=75"></span></div>"""

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
    sheet_name = "compareandrecycle"

    if '/yashin' in os.getcwd():
        filename = os.getcwd()+"/"+sheet_name+".csv"
    else:
        filename = '/home/admin/'+sheet_name+".csv"

    alreadyscrapped = []
    firefox_options = Options()
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)

    driver.set_page_load_timeout(10)

    with open(filename,"a",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp','link','Make Model','Capacity','Condition','recycler 1','price 1','recycler 2','price 2','recycler 3','price 3',
                         'gbp_hkd_rate','gbp_aud_rate'])


    gbp_hkd_rate = requests.post(
        "https://wise.com/gateway/v3/quotes/",
        json={
            "sourceAmount": 100,
            "sourceCurrency": "GBP",
            "targetCurrency": "HKD",
            "preferredPayIn": None,
            "guaranteedTargetAmount": False,
            "type": "REGULAR",
        },
    ).json()['rate']

    print("GBP -> HKD Rate: ")
    print(gbp_hkd_rate)

    gbp_aud_rate = requests.post(
        "https://wise.com/gateway/v3/quotes/",
        json={
            "sourceAmount": 100,
            "sourceCurrency": "GBP",
            "targetCurrency": "AUD",
            "preferredPayIn": None,
            "guaranteedTargetAmount": False,
            "type": "REGULAR",
        },
    ).json()['rate']

    print("GBP -> AUD Rate: ")
    print(gbp_aud_rate)



    driver.get("https://www.compareandrecycle.co.uk/search?page=1&productType=1")
    time.sleep(3)

    brands = Selector(text=a).xpath('.//*[@class="brand-box "]/img/@alt').extract()
    print(brands)

    for brand in brands:
        driver.get("https://www.compareandrecycle.co.uk/search?page=1&productType=1")
        time.sleep(3)
        driver.find_element(By.XPATH,f'.//img[@alt="{brand}"]').click()
        time.sleep(3)

        ds = Selector(text=driver.page_source).xpath('.//*[@class="product-wrap"]').extract()
        for d in ds:
            sel1 = Selector(text=d)
            l = sel1.xpath('.//a/@href').extract_first()
            product_name = ''.join(sel1.xpath('.//*[@class="product-name"]/text()').extract())

            for condition in ['new','working','working-poor','broken']:
                for capacity in ['64gb','128gb','256gb','512gb']:
                    if "https://www.compareandrecycle.co.uk"+l+"?condition="+str(condition)+"&capacity="+capacity not in alreadyscrapped:

                        try:
                            driver.get("https://www.compareandrecycle.co.uk"+l+"?condition="+str(condition)+"&capacity="+capacity)
                        except TimeoutException:
                            pass

                        time.sleep(3)
                        response = Selector(text=driver.page_source)
                        datas = response.xpath('.//*[@id="comparison-table"]/div[@class="comparison-row "]').extract()[:3]
                        temp = []
                        for data in datas:
                            sel = Selector(text=data)
                            recycler = sel.xpath('.//*[@class="comparison-cell merchant"]/img/@alt').extract_first()
                            try:
                                price = ''.join(re.findall(r'\d|\.', ''.join(sel.xpath('.//*[@class="comparison-cell price sort"]//text()').extract())))
                            except:
                                price = ''

                            temp.append(recycler)
                            temp.append(price)

                        temp += [None]*(6-len(temp))

                        cond = condition
                        if condition == "working":
                            cond = "good"
                        elif condition == "working-poor":
                            cond = "poor"


                        if temp:
                            with open(filename,"a",newline="",encoding="utf-8") as f:
                                writer = csv.writer(f)
                                writer.writerow([datetime.datetime.now().strftime("%Y-%m-%d (%H:%M)"),"https://www.compareandrecycle.co.uk"+l+"?condition="+str(condition)+"&capacity="+capacity,product_name,capacity,cond]+temp+[gbp_hkd_rate,gbp_aud_rate])
                                print([datetime.datetime.now().strftime("%Y-%m-%d (%H:%M)"),"https://www.compareandrecycle.co.uk"+l+"?condition="+str(condition)+"&capacity="+capacity,product_name,capacity,cond]+temp+[gbp_hkd_rate,gbp_aud_rate])

                    else:
                        print("Exists...")
    driver.close()

    uploadtospreadsheet()

