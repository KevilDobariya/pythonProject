from selenium.webdriver.common.by import By
from POM.Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

    def click_welcome_link(self):
        self.driver.find_element(by=By.ID, value=Locators.welcome_link_id).click()

    def click_logout_button(self):
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=Locators.logout_link_linktext).click()