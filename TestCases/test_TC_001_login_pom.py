from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Base import InitDriver
from Config.Config import  TestData
import time

from Library.ConfigReader import readele
from Pages import LoginPage
from Pages.LoginPage import LoginClass
import pytest
from DataDriven.TestData import DataGen
#///////////////////////////////////////////////////#
# def DataGen():
#     dt=[['reddy.csri@gmail.com','Csrireddy77!'],['jk','abcdc']]
#     return dt

# @pytest.mark.parametrize('datas',DataGen())
#///////////////////////////////////////////////////////#
@pytest.mark.parametrize('datas1',DataGen())
def test_login(datas1):

    driver=InitDriver.setBrowser()
    login_pg=LoginPage.LoginClass(driver)
    login_pg.enter_username(datas1[0])
    login_pg.enter_password(datas1[1])
    time.sleep(4)
    login_pg.click_login()
    time.sleep(6)


