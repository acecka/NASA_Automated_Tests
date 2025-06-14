from Tests.base_test import BaseTest
from Pages.home_page import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class VerifyPages(BaseTest):
    def setUp(self):
        super().setUp()

    def testValidPage(self):
        """
        Verifies the page title
        """
        self.assertIn("NASA", self.driver.title, "NASA not found in the title of the page")

    def testGoToNews(self):
        """
        Checks News & Events navigation menu accuracy
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.NEWS_N_EVENTS_LIST))
        self.home_page.expand_news()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.NEWS_N_EVENTS))
        self.home_page.click_news()
        self.assertIn("NASA News", self.driver.title)
        self.assertIn("NASA News", self.driver.find_element(*HomePageLocators.NEWS_PAGE_TITLE).text)

    def testGoToMultimedia(self):
        """
        Checks Multimedia navigation menu accuracy
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.MULTIMEDIA_LIST))
        self.home_page.expand_multimedia()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.MULTIMEDIA))
        self.home_page.click_multimedia()
        self.assertIn("Multimedia - NASA", self.driver.title)
        self.assertIn("Multimedia", self.driver.find_element(*HomePageLocators.MULTIMEDIA_PAGE_TITLE).text)

    def testGoToNASAPlus(self):
        """
        Checks NASA+ navigation menu accuracy
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.NASA_PLUS))
        self.home_page.click_nasa_plus()
        self.assertIn("Home | NASA+", self.driver.title, "Failed to navigate to NASA+ page")

    def tearDown(self):
        self.driver.quit()


