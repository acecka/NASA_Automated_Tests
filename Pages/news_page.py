from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class NewsPageLocators:
    NEWS1_PANEL = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[1]/a')
    NEWS1_PANEL_TITLE = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[1]/a/div/div/div[2]/p/span')
    NEWS2_PANEL = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[2]/a')
    NEWS2_PANEL_TITLE = (By.XPATH, '//*[@id="post-128945"]/div/div[3]/div/div[2]/div[1]/div[2]/a/div/div/div[2]/p/span')
    NEWS3_PANEL = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[2]/div/a[1]')
    NEWS4_PANEL = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[2]/div/a[2]')
    ARTICLE_TITLE = (By.XPATH, '/html/body/main/article/section/div[1]/div[2]/div/div/div/h1')


class NewsPage(BasePage):
    def click_blog1(self):
        self.driver.find_element(*NewsPageLocators.NEWS1_PANEL).click()

    def get_article_title(self):
        return self.driver.find_element(*NewsPageLocators.ARTICLE_TITLE).text


