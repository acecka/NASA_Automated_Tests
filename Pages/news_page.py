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

    ARTICLE_PANEL = (By.XPATH, '//*[@id="post-860982"]/section/div[2]/div[2]/div/div/div/div/figure/a/img')


class NewsPage(BasePage):

    def get_article_img(self):
        self.driver.find_element(*NewsPageLocators.ARTICLE_PANEL).get_attribute("img")

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

    def get_article_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NewsPageLocators.ARTICLE_TITLE)
        )
        return self.driver.find_element(*NewsPageLocators.ARTICLE_TITLE).text




