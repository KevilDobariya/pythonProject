import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import HtmlTestRunner

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service("../Drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        # cls.driver = webdriver.Chrome("../Drivers/chromedriver.exe")
        cls.driver.get("https://cloud.tenable.com/tio/app.html#/login")
        cls.driver.maximize_window()

    def test_login(self):
        self.driver.find_element(by=By.NAME, value = "username").send_keys("war@tenable.com")
        print("Username entered successfully")
        self.driver.find_element(by=By.NAME, value = "password").send_keys("50ad101b-8c7c-4ecf-873e-ceec15c2f578")
        print("Password entered successfully")
        self.driver.find_element(by=By.XPATH, value = "//*[@id='main-app']/div[1]/div/div[1]/div/form/div[3]/div[2]/button").click()
        print("Login button click action performed successfully")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/kevil_dobariya/PycharmProjects/pythonProject/Reports"))
