from Tests.base_test import BaseTest
from Pages.news_page import NewsPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

        # ensure image is present
        self.assertTrue(self.news_page.get_article_image(), "Missing image attribute")

        # ensure article has content in its paragraphs and they are not empty
        self.assertTrue(self.news_page.check_article_content(),
                        "The article does not have valid content in <p> elements.")

    def testVerifyNewsPanel2(self):
        """
        Checks Blog 2 navigation menu accuracy
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NewsPageLocators.NEWS2_PANEL))

        news2_url = self.news_page.get_news2_href()
        self.assertIsNotNone(news2_url, "Missing href attribute")

        news_title = self.news_page.get_news2_panel_title()

        # navigate to the URL
        self.news_page.click_news2()

        # ensure actual navigation is correct
        self.assertEqual(self.driver.current_url, news2_url, "URL mismatch")

        # ensure article title is correct
        article_title = self.news_page.get_article_title()
        self.assertEqual(news_title, article_title, "Title mismatch")

        # ensure image is present
        self.assertTrue(self.news_page.get_article_image(), "Missing image attribute")

        # ensure article has content in its paragraphs and they are not empty
        self.assertTrue(self.news_page.check_article_content(),
                        "The article does not have valid content in <p> elements.")

    def testVerifyNewsPanel3(self):
        """
        Checks Blog 3 navigation menu accuracy
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NewsPageLocators.NEWS3_PANEL))

        news3_url = self.news_page.get_news3_href()
        self.assertIsNotNone(news3_url, "Missing href attribute")

        news_title = self.news_page.get_news3_panel_title()

        # navigate to the URL
        self.news_page.click_news3()

        # ensure actual navigation is correct
        self.assertEqual(self.driver.current_url, news3_url, "URL mismatch")

        # ensure article title is correct
        article_title = self.news_page.get_article_title()
        self.assertEqual(news_title, article_title, "Title mismatch")

        # ensure image is present
        self.assertTrue(self.news_page.get_article_image(), "Missing image attribute")

        # ensure article has content in its paragraphs and they are not empty
        self.assertTrue(self.news_page.check_article_content(),
                        "The article does not have valid content in <p> elements.")

    def testVerifyNewsPanel4(self):
        """
        Checks Blog 4 navigation menu accuracy
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NewsPageLocators.NEWS4_PANEL))

        news4_url = self.news_page.get_news4_href()
        self.assertIsNotNone(news4_url, "Missing href attribute")

        news_title = self.news_page.get_news4_panel_title()

        # navigate to the URL
        self.news_page.click_news4()

        # ensure actual navigation is correct
        self.assertEqual(self.driver.current_url, news4_url, "URL mismatch")

        # ensure article title is correct
        # article_title = self.news_page.get_article_title()
        # self.assertEqual(news_title, article_title, "Title mismatch")

        # ensure image is present
        self.assertTrue(self.news_page.get_article_image(), "Missing image attribute")

        # ensure article has content in its paragraphs and they are not empty
        self.assertTrue(self.news_page.check_article_content(),
                        "The article does not have valid content in <p> elements.")
