from Tests.base_test import BaseTest
from Pages.news_page import NewsPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewsPageTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.news_page = self.home_page.expand_news()
        self.news_page = self.home_page.click_news()

    def testGoToBlog1(self):
        """
        Checks Blog 1 navigation menu accuracy
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(NewsPageLocators.BLOG1_BLOCK))

        block1_url = self.driver.find_element(*NewsPageLocators.BLOG1_BLOCK)
        block1_link = block1_url.get_attribute("href")
        self.assertIsNotNone(block1_link, "Missing href attribute")
        # navigate to the URL
        self.news_page.click_blog1()
        # ensure actual navigation is correct
        block_navigation = self.driver.current_url
        self.assertEqual(block_navigation, block1_link, "URL mismatch")


