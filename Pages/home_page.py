from Pages.base_page import BasePage
from Pages.news_page import NewsPage
from Pages.nasaplus_page import NasaPlusPage
from Pages.multi_page import MultimediaPage
from selenium.webdriver.common.by import By


class HomePageLocators:
    NEWS_N_EVENTS_LIST = (By.XPATH, '/html/body/header[2]/div/nav/div/ul/li[1]/button')
    NEWS_N_EVENTS = (By.XPATH, '/html/body/header[2]/div/nav/div/ul/li[1]/ul/a')
    NEWS_PAGE_TITLE = (By.XPATH, '/html/body/main/article/div/div[2]/div[2]/div/div[1]/h1')
    MULTIMEDIA_LIST = (By.XPATH, '/html/body/header[2]/div/nav/div/ul/li[2]/button')
    MULTIMEDIA = (By.XPATH, '/html/body/header[2]/div/nav/div/ul/li[2]/ul/a')
    MULTIMEDIA_PAGE_TITLE = (By.XPATH, '/html/body/main/article/div/div[2]/div/div/div[1]/h1')
    NASA_PLUS = (By.XPATH, '//header[2]/div/nav/div/ul/li[3]/a')

    SEARCH_BOX = (By.ID, "search-field-en-small--desktop")
    SEARCH_RESULTS1 = (By.XPATH, '//div[2]/div[3]/div/a')
    SEARCH_RESULTS_ALL = (By.XPATH, '//main/div/div[2]/div/div[2]')

    EXPLORE_EXPAND = (By.ID, "global-navigation-trigger")
    EXPLORE_MISSIONS = By.XPATH, "//body/div[2]/div/div/div[1]/div/ul/li[2]/a"
    EXPLORE_MISSIONS_MAIN = (By.XPATH, '//div[2]/div/div/div[3]/div/div[2]/a')

    EXPLORE_UNIVERSE = (By.XPATH, "//body/div[2]/div/div/div[1]/div/ul/li[6]/a")
    EXPLORE_UNIVERSE_MAIN = (By.XPATH, '//div[2]/div/div/div[3]/div/div[6]/a')


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

    def click_nasa_plus(self):
        self.driver.find_element(*HomePageLocators.NASA_PLUS).click()
        return NasaPlusPage(self.driver)

    def get_missions_url(self):
        return self.driver.find_element(*HomePageLocators.EXPLORE_MISSIONS_MAIN).get_attribute("href")

    def get_universe_url(self):
        return self.driver.find_element(*HomePageLocators.EXPLORE_UNIVERSE_MAIN).get_attribute("href")
