from Tests.base_test import BaseTest
from Pages.multi_page import MultiPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MultiPageTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.multi_page = self.home_page.expand_multimedia()
        self.multi_page = self.home_page.click_multimedia()

    def testMultiPanel1(self):
        pass
