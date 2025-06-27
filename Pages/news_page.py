from selenium.webdriver import ActionChains

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
        news1 = self.driver.find_element(*NewsPageLocators.NEWS1_PANEL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", news1)
        ActionChains(self.driver).move_to_element(news1).perform()
        news1.click()

    def click_news2(self):
        news2 = self.driver.find_element(*NewsPageLocators.NEWS2_PANEL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", news2)
        ActionChains(self.driver).move_to_element(news2).perform()
        news2.click()

    def click_news3(self):
        news3 = self.driver.find_element(*NewsPageLocators.NEWS3_PANEL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", news3)
        ActionChains(self.driver).move_to_element(news3).perform()
        news3.click()

    def click_news4(self):
        news4 = self.driver.find_element(*NewsPageLocators.NEWS4_PANEL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", news4)
        ActionChains(self.driver).move_to_element(news4).perform()
        news4.click()

    def get_news1_href(self):
        news1_url = self.driver.find_element(*NewsPageLocators.NEWS1_PANEL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", news1_url)
        ActionChains(self.driver).move_to_element(news1_url).perform()
        return news1_url.get_attribute("href")

    def get_news2_href(self):
        news2_url = self.driver.find_element(*NewsPageLocators.NEWS2_PANEL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", news2_url)
        ActionChains(self.driver).move_to_element(news2_url).perform()
        return news2_url.get_attribute("href")

    def get_news3_href(self):
        news3_url = self.driver.find_element(*NewsPageLocators.NEWS3_PANEL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", news3_url)
        ActionChains(self.driver).move_to_element(news3_url).perform()
        return news3_url.get_attribute("href")

    def get_news4_href(self):
        news4_url = self.driver.find_element(*NewsPageLocators.NEWS4_PANEL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", news4_url)
        ActionChains(self.driver).move_to_element(news4_url).perform()
        return news4_url.get_attribute("href")

    def get_news1_panel_title(self):
        news1_title = self.driver.find_element(*NewsPageLocators.NEWS1_PANEL_TITLE)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", news1_title)
        ActionChains(self.driver).move_to_element(news1_title).perform()
        return news1_title.text

    def get_news2_panel_title(self):
        news2_title = self.driver.find_element(*NewsPageLocators.NEWS2_PANEL_TITLE)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", news2_title)
        ActionChains(self.driver).move_to_element(news2_title).perform()
        return news2_title.text

    def get_news3_panel_title(self):
        news3_title = self.driver.find_element(*NewsPageLocators.NEWS3_PANEL_TITLE)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", news3_title)
        ActionChains(self.driver).move_to_element(news3_title).perform()
        return news3_title.text

    def get_news4_panel_title(self):
        news4_title = self.driver.find_element(*NewsPageLocators.NEWS4_PANEL_TITLE)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", news4_title)
        ActionChains(self.driver).move_to_element(news4_title).perform()
        return news4_title.text
