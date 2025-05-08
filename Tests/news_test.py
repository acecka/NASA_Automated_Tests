from Tests.base_test import BaseTest
from Pages.news_page import NewsPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class NewsPageTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.news_page = self.home_page.expand_news()
        self.news_page = self.home_page.click_news()

    def testVerifyNewsPanel1(self):
        """
        Checks Blog 1 navigation menu accuracy
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NewsPageLocators.NEWS1_PANEL))

        news1_url = self.news_page.get_news1_href()
        self.assertIsNotNone(news1_url, "Missing href attribute")

        news_title = self.news_page.get_news1_panel_title()

        # navigate to the URL
        self.news_page.click_news1()

        # ensure actual navigation is correct
        self.assertEqual(self.driver.current_url, news1_url, "URL mismatch")

        # ensure article title is correct
        article_title = self.news_page.get_article_title()
        self.assertEqual(news_title, article_title, "Title mismatch")
        sleep(2)


