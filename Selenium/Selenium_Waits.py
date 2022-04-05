from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
driver.get("https://www.google.com/")
driver.maximize_window()

# implicit wait
# driver.implicitly_wait(10)

driver.find_element(by=By.NAME, value="q").send_keys("Tools QA")

wait = WebDriverWait(driver, 10)
try:
    element = wait.until(EC.element_to_be_clickable((By.NAME, "btnK1")))
    print("Element is clickable")
    element.click()
except:
    print("Element is not clickable")
# driver.find_element(by=By.NAME, value="btnK1").click()

driver.close()
driver.quit()
