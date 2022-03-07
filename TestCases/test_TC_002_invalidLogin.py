from selenium.webdriver.common.by import By

from Base import  InitDriver

def test_invalidlogin():
    driver=InitDriver.setBrowser()
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys("csr@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"input[name='pass']").send_keys('srik1234')
    driver.find_element(By.XPATH, "//button[text()='Log In']").click()