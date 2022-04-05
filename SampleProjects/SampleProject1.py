from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner

class SampleProject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = Service("../Drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.s)
        cls.driver.maximize_window()
        # Implemented implicit wait
        cls.driver.implicitly_wait(10)

    def test_Login(self):
        self.driver.get("https://cloud.tenable.com/")
        self.driver.find_element(by=By.NAME, value="username").send_keys("war@tenable.com")
        print("Username entered successfully")
        self.driver.find_element(by=By.NAME, value="password").send_keys("50ad101b-8c7c-4ecf-873e-ceec15c2f578")
        print("Password entered successfully")
        self.driver.find_element(by=By.XPATH, value="//button[@type='submit1']").click()
        print("Click action performed successfully")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

# Used for running from commnand line
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/kevil_dobariya/PycharmProjects/pythonProject/Reports"))




