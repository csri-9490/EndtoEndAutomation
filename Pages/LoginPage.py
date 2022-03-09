from selenium.webdriver.common.by import By

from Library import ConfigReader

class  LoginClass:
    def __init__(self,obj1):
        global driver
        driver=obj1
    def enter_username(self,username):
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys(username)

    def enter_password(self,password):
        driver.find_element(By.CSS_SELECTOR, "input[name='pass']").send_keys(password)

    def click_login(self):
        driver.find_element(By.XPATH, "//button[text()='Log In']").click()