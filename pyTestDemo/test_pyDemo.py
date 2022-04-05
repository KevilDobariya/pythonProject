from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class Test_pydemo():

    # @pytest.mark.skip
    @pytest.fixture()
    def test_setUp(self):
        global driver
        s = Service("../Drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    # @pytest.fixture()
    def test_Login(self, test_setUp):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(by=By.ID, value="txtUsername").send_keys("Admin")
        print("Username entered")
        driver.find_element(by=By.ID, value="txtPassword").send_keys("admin123")
        print("Password entered")
        driver.find_element(by=By.ID, value="btnLogin").click()
        print("Login button clicked")

    # @pytest.mark.skip(reason="No need to run this test")
    def test_Welcome(self,test_setUp):
        self.test_Login(test_setUp)
        driver.find_element(by=By.ID, value="welcome").click()
        print("Welcome link clicked")
        driver.find_element(by=By.LINK_TEXT, value="Logout1").click()
        print("Logout link clicked")

    # def sum(self, a ,b):
    #     return a+b
    #
    # @pytest.mark.parametrize("input1, input2, total",
    #                          [(2, 5, 7),
    #                           (5, 5, 10)]
    #                          )
    # def test_addition(self, input1, input2, total):
    #     result = self.sum(input1, input2)
    #     assert result == total
    #     print(total)

    @pytest.mark.skip
    def test_run(self):
        print("run")



