import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager import  *
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


class Test1:
    @pytest.mark.parametrize("username,password",[("selenium","webdriver"),("python","pytest"),("sri","kanth")])
    def test_data(self,username,password):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys(username)
        time.sleep(5)


