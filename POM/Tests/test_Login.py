from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM.Pages.login_Page import LoginPage
from POM.Pages.home_Page import HomePage
import HtmlTestRunner

class test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_Log(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login_button()

        home = HomePage(driver)
        home.click_welcome_link()
        home.click_logout_button()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/kevil_dobariya/PycharmProjects/pythonProject/Reports"))
