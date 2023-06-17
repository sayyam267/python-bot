import csv
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://www.adultdvdmarketplace.com/xcart/adult_dvd/disclaimer.php')
enter = driver.find_element(By.LINK_TEXT,"ENTER").click()
# sleep(2)
username = driver.find_element(By.XPATH,'//input[@id="username"]').send_keys('DVDuniverse')
password = driver.find_element(By.XPATH,'//input[@id="password"]').send_keys('monstA1011')
signin = driver.find_element(By.XPATH,'//div/button[@type="submit"]').click()
while True:
    for pag in range(1,673):
        driver.get(f'https://www.adultdvdmarketplace.com/xcart/adult_dvd/modify_listings.php?sort=&&page={pag}')
        boss = driver.find_elements(By.XPATH,'//tbody/tr')
        links = []
        prices = []
        for cx in boss:
            inputbox = cx.find_elements(By.XPATH,'//td[@valign="top"]/a[2]')
            marktprice = cx.find_elements(By.XPATH,'//td[@align="center"][2]')
        for h,mhh in zip(inputbox,marktprice):
            ham = h.get_attribute('href')
            links.append(ham)
            prices.append(mhh.text)
        for link,price in zip(links,prices):
            try:m_pp = float(price.split('$')[-1].split(' ')[0].strip())
            except:m_pp = 'n'
            try:send_mo = str(m_pp - 0.001)
            except:send_mo = ''
            if m_pp == 'n':
                continue
            else:
                print('Else')
                try:send_m = send_mo.split('.')[-1][0:2]
                except:send_m = '95'
                try:send_mm = send_mo.split('.')[0]
                except:send_mm = '29'
                driver.get(link)
                mr = driver.find_element(By.XPATH,'//div[@class="form-group"][3]//input[@type="text"]').send_keys(Keys.CONTROL+'A')
                driver.find_element(By.XPATH,'//div[@class="form-group"][3]//input[@type="text"]').send_keys(f'{send_mm}.{send_m}')
                driver.find_element(By.XPATH,'//p[@align="center"]//button[@type="submit"]').click()