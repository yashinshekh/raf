# driver.get("https://wise.com/wishes/")
# time.sleep(2)
# driver.find_element(By.ID,'tw-calculator-source-select').click()
# driver.find_element(By.ID,'tw-calculator-source-select-searchbox').send_keys('GBP')
# ActionChains(driver).send_keys(Keys.ENTER).perform()
# time.sleep(2)
# driver.get("https://wise.com/")
# driver.find_element(By.ID,'tw-calculator-target-select').click()
# driver.find_element(By.ID,'tw-calculator-target-select-searchbox').send_keys('HKD')
# ActionChains(driver).send_keys(Keys.ENTER).perform()
# time.sleep(2)
# gbp_hkd_rate = Selector(text=driver.page_source).xpath('.//*[@class="tw-calculator-breakdown-rate__value"]/text()').extract_first()
#
# print("GBP -> HKD Rate: ")
# print(gbp_hkd_rate)
#
#
# driver.find_element(By.ID,'tw-calculator-source-select').click()
# driver.find_element(By.ID,'tw-calculator-source-select-searchbox').send_keys('GBP')
# ActionChains(driver).send_keys(Keys.ENTER).perform()
# time.sleep(2)
# driver.get("https://wise.com/")
# driver.find_element(By.ID,'tw-calculator-target-select').click()
# ActionChains(driver).send_keys(Keys.ENTER).perform()
# time.sleep(2)
# gbp_aud_rate = Selector(text=driver.page_source).xpath('.//*[@class="tw-calculator-breakdown-rate__value"]/text()').extract_first()
#
# print("GBP -> AUD Rate: ")
# print(gbp_aud_rate)