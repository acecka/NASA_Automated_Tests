from Pages.base_page import BasePage
from Pages.news_page import NewsPage
from Pages.multi_page import MultimediaPage
from selenium.webdriver.common.by import By


class HomePageLocators:
    NEWS_N_EVENTS_LIST = (By.XPATH, '/html/body/header[2]/div/nav/div/ul/li[1]/button')
    NEWS_N_EVENTS = (By.XPATH, '/html/body/header[2]/div/nav/div/ul/li[1]/ul/a')
    NEWS_PAGE_TITLE = (By.XPATH, '/html/body/main/article/div/div[2]/div[2]/div/div[1]/h1')
    MULTIMEDIA_LIST = (By.XPATH, '/html/body/header[2]/div/nav/div/ul/li[2]/button')
    MULTIMEDIA = (By.XPATH, '/html/body/header[2]/div/nav/div/ul/li[2]/ul/a')
    MULTIMEDIA_PAGE_TITLE = (By.XPATH, '/html/body/main/article/div/div[2]/div/div/div[1]/h1')


class HomePage(BasePage):
    def expand_news(self):
        self.driver.find_element(*HomePageLocators.NEWS_N_EVENTS_LIST).click()

    def click_news(self):
        self.driver.find_element(*HomePageLocators.NEWS_N_EVENTS).click()
        return NewsPage(self.driver)

    def expand_multimedia(self):
        self.driver.find_element(*HomePageLocators.MULTIMEDIA_LIST).click()

    def click_multimedia(self):
        self.driver.find_element(*HomePageLocators.MULTIMEDIA).click()
        return MultimediaPage(self.driver)
