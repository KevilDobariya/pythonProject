import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("../Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()

driver.get("https://cloud.tenable.com/")

time.sleep(5)

driver.find_element(by=By.NAME, value="username").send_keys("war@tenable.com")

driver.find_element(by=By.NAME, value="password").send_keys("50ad101b-8c7c-4ecf-873e-ceec15c2f578")

driver.find_element(by=By.XPATH, value="//*[@id='main-app']/div[1]/div/div[1]/div/form/div[3]/div[2]/button").click()

time.sleep(3)

driver.close()
driver.quit()

print("Browser launch and login action performed successfully")