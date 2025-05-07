from selenium import webdriver
from Pages.home_page import HomePage
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://nasa.gov/")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()
