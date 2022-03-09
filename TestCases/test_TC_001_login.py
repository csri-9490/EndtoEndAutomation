from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Base import InitDriver
from Config.Config import  TestData
import time

from Library.ConfigReader import readele


def test_login():

    driver=InitDriver.setBrowser()
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys(readele("sigin","USER_NAME"))
    driver.find_element(By.CSS_SELECTOR,"input[name='pass']").send_keys(TestData.PASSWORD)
    driver.find_element(By.XPATH,"//button[text()='Log In']").click()


