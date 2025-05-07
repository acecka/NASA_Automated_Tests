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

        news1_url = self.driver.find_element(*NewsPageLocators.NEWS1_PANEL)
        news1_link = news1_url.get_attribute("href")
        self.assertIsNotNone(news1_link, "Missing href attribute")
        news_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NewsPageLocators.NEWS1_PANEL_TITLE)).text
        # navigate to the URL
        self.news_page.click_blog1()
        # ensure actual navigation is correct
        panel_navigation = self.driver.current_url
        self.assertEqual(panel_navigation, news1_link, "URL mismatch")
        # ensure article title is correct
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NewsPageLocators.ARTICLE_TITLE))
        article_title = self.news_page.get_article_title()
        # article_title = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(NewsPageLocators.ARTICLE_TITLE)).text
        self.assertEqual(news_title, article_title, "Title mismatch")
        sleep(2)


