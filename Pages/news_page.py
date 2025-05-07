from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class NewsPageLocators:
    BLOG1_BLOCK = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[1]/a')
    BLOG1_TITLE = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[1]/a/div/div/div[2]/p/span')
    BLOG2_BLOCK = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[2]/a')
    BLOG3_BLOCK = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[2]/div/a[1]')
    BLOG4_BLOCK = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[2]/div/a[2]')


class NewsPage(BasePage):
    def click_blog1(self):
        self.driver.find_element(*NewsPageLocators.BLOG1_BLOCK).click()
