from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.service import Service
from Config import Config
from Config.Config import TestData
# from Library import ConfigReader
# from Library import ConfigReader
from Library.ConfigReader import readConfigData
def setBrowser():

    op = Options()
    op.add_argument('--disable-notifications')
    global driver
    if((readConfigData('Details','Browser'))=="Chrome"):
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=op)
    else:
    #elif((ConfigReader.readConfigData('Details','Browser'))=="firefox"):
        driver=webdriver.firefox(executable_path="D:\\drivers\\geckodriver.exe")
    driver.get(readConfigData('Details','URL'))
    driver.maximize_window()
    return driver

    # yield
    # driver.close()
    # return setBrowser
