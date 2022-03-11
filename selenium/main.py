from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from config import *

driver = webdriver.Firefox()
driver.get('https://portal.visioniot.net/view/#/')
# assert "Twitter." in driver.title


class MXVision:
    def __init__(self, username: str, password: str):
        self.driver = webdriver.Firefox()

        # login info
        self.username = username
        self.password = password


    def login(self):
        driver = self.driver
        self.driver.get('https://portal.visioniot.net/view/#/')
        self.un = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div/div[2]/div[1]/div/input')
        self.pw = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div/div[2]/div[2]/div/input')
        self.sb = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div/div[3]/div[1]/button/span[1]')
        self.un.send_keys(self.username)
        self.pw.send_keys(self.password)
        self.sb.click()

    def create_program(self):
        driver = self.driver
        sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/ul/li[6]/a/div').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/a[1]/div/button/div[1]/span[1]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/span[1]/button').click()
        sleep(2)
        # prg_name = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div[1]/form/div[1]/div/div[2]/div/span/div/input')
        prg_name = driver.find_element_by_class_name('ant-input').send_keys('Test Program')
        prg_valid_from = driver.find_element_by_name('ValidFrom').send_keys('24-02-2022')
        prg_valid_to = driver.find_element_by_name('ValidTo').send_keys('31-03-2022')
        add = driver.find_element_by_css_selector('.ant-col-24 > button:nth-child(1)').click()


session = MXVision(MX_UN, MX_PW)
session.login()
session.create_program()

"""
try:
    # els = driver.find_elements(By.TAG_NAME, 'input')
    un = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div/div[2]/div[1]/div/input')
    pw = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div/div[2]/div[2]/div/input')
    un.send_keys(MX_UN)
    pw.send_keys(MX_PW)
    sb = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div/div[3]/div[1]/button/span[1]').click()
    # sb.send_keys(Keys.RETURN)

    with open('page.html', 'w') as pg:
        pg.write(driver.page_source)


except Exception as e:
    print(e)

"""

# el.clear()
# el.send_keys('pycon')
# el.send_keys(Keys.RETURN)
# assert "No Results Found" not in driver.page_source
# driver.close()
