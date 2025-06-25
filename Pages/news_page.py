from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class NewsPageLocators:
    NEWS1_PANEL = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[1]/a')
    NEWS1_PANEL_TITLE = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[1]/a/div/div/div[2]/p/span')
    NEWS2_PANEL = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[2]/a')
    NEWS2_PANEL_TITLE = (By.XPATH, '//*[@id="post-128945"]/div/div[3]/div/div[2]/div[1]/div[2]/a/div/div/div[2]/p/span')
    NEWS3_PANEL = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[2]/div/a[1]')
    NEWS3_PANEL_TITLE = (By.XPATH, '//*[@id="post-128945"]/div/div[3]/div/div[2]/div[1]/div[2]/div/a[1]/div/div/div[2]/p/span')
    NEWS4_PANEL = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[2]/div/a[2]')
    NEWS4_PANEL_TITLE = (By.XPATH, '//*[@id="post-128945"]/div/div[3]/div/div[2]/div[1]/div[2]/div/a[2]/div/div/div[2]/p/span')

    ARTICLE_TITLE = (By.XPATH, '/html/body/main/article/section/div[1]/div[2]/div/div/div/h1')
    ARTICLE_IMAGE_PANEL = (By.XPATH, '//section/div[2]/div[2]/div/div/div/div/figure/a')
    ARTICLE_CONTENT = (By.XPATH, '//section/div[2]/div[2]/div')

    BLOG_TITLE = (By.XPATH, '//h1')
    BLOG_IMAGE_PANEL = (By.XPATH, '//div[1]/div/div/figure/a')
    # BLOG_CONTENT = (By.CLASS_NAME, 'single-blog-content')
    BLOG_CONTENT = (By.XPATH, '//div[4]/article/div[2]/div')


class NewsPage(BasePage):

    def get_article_title(self):
        panel_url = self.driver.current_url
        if "news-release" in panel_url:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(NewsPageLocators.ARTICLE_TITLE)
            )
            return self.driver.find_element(*NewsPageLocators.ARTICLE_TITLE).text
        elif "blogs" in panel_url:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(NewsPageLocators.BLOG_TITLE)
            )
            return self.driver.find_element(*NewsPageLocators.BLOG_TITLE).text
        else:
            raise ValueError("Unknown news type in URL")

    def get_article_image(self):
        panel_url = self.driver.current_url
        if "news-release" in panel_url:
            img_panel = self.driver.find_element(*NewsPageLocators.ARTICLE_IMAGE_PANEL)
            img_element = img_panel.find_element(By.TAG_NAME, "img")
            return img_element.get_attribute("src")
        elif "blogs" in panel_url:
            img_panel = self.driver.find_element(*NewsPageLocators.BLOG_IMAGE_PANEL)
            img_element = img_panel.find_element(By.TAG_NAME, "img")
            return img_element.get_attribute("src")
        else:
            raise ValueError("Unknown news type in URL")

    def check_article_content(self):
        panel_url = self.driver.current_url
        if "news-release" in panel_url:
            article_panel = self.driver.find_element(*NewsPageLocators.ARTICLE_CONTENT)
            return article_panel.find_elements(By.TAG_NAME, "p")
        elif "blogs" in panel_url:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(NewsPageLocators.BLOG_CONTENT)
            )
            blog_panel = self.driver.find_element(*NewsPageLocators.BLOG_CONTENT)
            return blog_panel.find_elements(By.TAG_NAME, "p")
        else:
            raise ValueError("Unknown news type in URL")

    def click_news1(self):
        self.driver.find_element(*NewsPageLocators.NEWS1_PANEL).click()

    def click_news2(self):
        self.driver.find_element(*NewsPageLocators.NEWS2_PANEL).click()

    def click_news3(self):
        self.driver.find_element(*NewsPageLocators.NEWS3_PANEL).click()

    def click_news4(self):
        self.driver.find_element(*NewsPageLocators.NEWS4_PANEL).click()

    def get_news1_href(self):
        return self.driver.find_element(*NewsPageLocators.NEWS1_PANEL).get_attribute("href")

    def get_news2_href(self):
        return self.driver.find_element(*NewsPageLocators.NEWS2_PANEL).get_attribute("href")

    def get_news3_href(self):
        return self.driver.find_element(*NewsPageLocators.NEWS3_PANEL).get_attribute("href")

    def get_news4_href(self):
        return self.driver.find_element(*NewsPageLocators.NEWS4_PANEL).get_attribute("href")

    def get_news1_panel_title(self):
        return self.driver.find_element(*NewsPageLocators.NEWS1_PANEL_TITLE).text

    def get_news2_panel_title(self):
        return self.driver.find_element(*NewsPageLocators.NEWS2_PANEL_TITLE).text

    def get_news3_panel_title(self):
        return self.driver.find_element(*NewsPageLocators.NEWS3_PANEL_TITLE).text

    def get_news4_panel_title(self):
        return self.driver.find_element(*NewsPageLocators.NEWS4_PANEL_TITLE).text
