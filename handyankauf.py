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


a = """<ul data-original-position="open-right" class="open-right" style="">
	<li class="imMnMnFirst imLevel" data-link-paths=",/apple-iphone-smartphone-verkaufen-seite-1.html" data-link-hash="-1004153238"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="apple-iphone-smartphone-verkaufen-seite-1.html" class="label" onclick="return x5engine.utils.location('apple-iphone-smartphone-verkaufen-seite-1.html', null, false)">Apple Iphone</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/blackberry-smartphone-verkaufen.html" data-link-hash="-1004156449"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="blackberry-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('blackberry-smartphone-verkaufen.html', null, false)">BlackBerry</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/google-smartphone-verkaufen.html" data-link-hash="-1004153504"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="google-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('google-smartphone-verkaufen.html', null, false)">Google</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/honor-smartphone-verkaufen.html" data-link-hash="-1004154929"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="honor-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('honor-smartphone-verkaufen.html', null, false)">Honor</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/huawei-smartphone-verkaufen.html" data-link-hash="-1004155043"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="huawei-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('huawei-smartphone-verkaufen.html', null, false)">Huawei</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/htc-smartphone-verkaufen.html" data-link-hash="-1004154948"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="htc-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('htc-smartphone-verkaufen.html', null, false)">HTC</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/lg-smartphone-verkaufen.html" data-link-hash="-1004155081"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="lg-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('lg-smartphone-verkaufen.html', null, false)">LG</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/nokia-smartphone-verkaufen.html" data-link-hash="-1004155062"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="nokia-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('nokia-smartphone-verkaufen.html', null, false)">Nokia</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/oneplus-smartphone-verkaufen.html" data-link-hash="-1004154834"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="oneplus-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('oneplus-smartphone-verkaufen.html', null, false)">OnePlus</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/samsung-smartphone-verkaufen.html" data-link-hash="-1004155024"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="samsung-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('samsung-smartphone-verkaufen.html', null, false)">Samsung</a></div></div></li><li class="imMnMnMiddle imLevel" data-link-paths=",/sony-smartphone-verkaufen.html" data-link-hash="-1004154986"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="sony-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('sony-smartphone-verkaufen.html', null, false)">Sony</a></div></div></li><li class="imMnMnLast imLevel" data-link-paths=",/xiaomi-smartphone-verkaufen.html" data-link-hash="-1004153485"><div class="label-wrapper"><div class="label-inner-wrapper"><a href="xiaomi-smartphone-verkaufen.html" class="label" onclick="return x5engine.utils.location('xiaomi-smartphone-verkaufen.html', null, false)">Xiaomi</a></div></div></li></ul>"""

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

def uploadtospreadsheet():
    creds = service_account.Credentials.from_service_account_file('credentials.json')

    # credentials, project = google.auth.default(scopes=['https://www.googleapis.com/auth/spreadsheets'])
    service = build('sheets', 'v4', credentials=creds)

    spreadsheet_id = spreadsheet_url.split('/')[-2]

    with open(os.getcwd()+"/raf/"+sheet_name+".csv") as csv_file:
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
    sheet_name = "handyankauf"

    alreadyscrapped = []
    firefox_options = Options()
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)

    with open(os.getcwd()+"/raf/"+sheet_name+".csv","a",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(['link','timestamp','brand','title','phone_name','storage','Like new','Very good','Good','In order','Inadequate','EUR -> AUD','EUR -> HKD'])

    scrapped_time = datetime.datetime.now().strftime("%Y-%m-%d (%H:%M)")

    driver.get("https://wise.com/")
    driver.find_element(By.ID,'tw-calculator-source-select').click()
    driver.find_element(By.ID,'tw-calculator-source-select-searchbox').send_keys('EUR')
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(1)
    driver.get("https://wise.com/")
    driver.find_element(By.ID,'tw-calculator-target-select').click()
    driver.find_element(By.ID,'tw-calculator-target-select-searchbox').send_keys('HKD')
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(1)
    eur_hkd_rate = Selector(text=driver.page_source).xpath('.//*[@class="tw-calculator-breakdown-rate__value"]/text()').extract_first()

    print(eur_hkd_rate)

    driver.find_element(By.ID,'tw-calculator-source-select').click()
    driver.find_element(By.ID,'tw-calculator-source-select-searchbox').send_keys('EUR')
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(1)
    driver.get("https://wise.com/")
    driver.find_element(By.ID,'tw-calculator-target-select').click()
    driver.find_element(By.ID,'tw-calculator-target-select-searchbox').send_keys('AUD')
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(1)
    eur_aud_rate = Selector(text=driver.page_source).xpath('.//*[@class="tw-calculator-breakdown-rate__value"]/text()').extract_first()

    print(eur_aud_rate)


    driver.get("https://handyankauf-online.at/")

    ds = Selector(text=a).xpath('.//a').extract()
    for d in ds:
        sel1 = Selector(text=d)
        brand = sel1.xpath('.//a/text()').extract_first()
        link = sel1.xpath('.//a/@href').extract_first()

        print("Link: "+str(link))
        driver.get("https://handyankauf-online.at/"+link)

        datas1 = Selector(text=driver.page_source).xpath('.//*[@class="fs10lh1-5 cf1"]').extract()
        for data1 in datas1:
            sel2 = Selector(text=data1)
            link_2 = sel2.xpath('.//a/@href').extract_first()
            title = sel2.xpath('.//a/text()').extract_first().replace('verkaufen','')


            driver.get("https://handyankauf-online.at/"+link_2)

            # phone_links = Selector(text=driver.page_source).xpath('.//button/@onclick[contains(.,"return x5engine.utils.imPopUpWin")]').extract()
            phone_links = Selector(text=driver.page_source).xpath('.//button/@onclick[contains(.,"return x5engine.utils.imPopUpWin")] | .//*[@class="fs10lh1-5 cf1"]/a/@href').extract()

            print(phone_links)

            for phone_link in phone_links:
                phone_link = phone_link.replace("return x5engine.utils.imPopUpWin('",'').replace("','imPopUp', 1000, 562);",'')
                phone_link = '/'+phone_link if '/script' not in phone_link else phone_link
                if "https://handyankauf-online.at"+phone_link not in alreadyscrapped:
                    try:
                        driver.get("https://handyankauf-online.at"+phone_link)

                        response = Selector(text=driver.page_source)

                        storage = response.xpath('.//h1/text()').extract_first().split()[-1]
                        phone_name = response.xpath('.//h1/text()').extract_first()
                        try:
                            phone_name = phone_name.replace(storage,'')
                        except:
                            pass

                        cond_prices = {"Wie neu":'',"Sehr Gut":'','Gut':'','In Ordnung':'','Mangelhaft':''}

                        for condition in ['Wie neu','Sehr Gut','Gut','In Ordnung','Mangelhaft']:
                            try:
                                Select(driver.find_element(By.XPATH,'.//*[@name="zustand"]')).select_by_visible_text(condition)
                                time.sleep(3)

                                cond_prices[condition] = ''.join(Selector(text=driver.page_source).xpath('.//*[@id="price"]/..//text()').extract())
                            except:
                                cond_prices[condition] = ''

                        with open(os.getcwd()+"/raf/"+sheet_name+".csv","a",newline="",encoding="utf-8") as f:
                            writer = csv.writer(f)
                            writer.writerow(["https://handyankauf-online.at"+phone_link,scrapped_time,brand,title,phone_name,storage]+list(cond_prices.values())+[eur_aud_rate,eur_hkd_rate])
                            print(["https://handyankauf-online.at"+phone_link,scrapped_time,brand,title,phone_name,storage]+list(cond_prices.values())+[eur_aud_rate,eur_hkd_rate])

                    except:
                        pass

    driver.close()

    uploadtospreadsheet()
