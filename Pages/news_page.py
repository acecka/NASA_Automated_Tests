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
    NEWS4_PANEL = (By.XPATH, '/html/body/main/article/div/div[3]/div/div[2]/div[1]/div[2]/div/a[2]')
    ARTICLE_TITLE = (By.XPATH, '/html/body/main/article/section/div[1]/div[2]/div/div/div/h1')


class NewsPage(BasePage):
    def click_news1(self):
        self.driver.find_element(*NewsPageLocators.NEWS1_PANEL).click()

    def get_news1_href(self):
        return self.driver.find_element(*NewsPageLocators.NEWS1_PANEL).get_attribute("href")

    def get_news1_panel_title(self):
        return self.driver.find_element(*NewsPageLocators.NEWS1_PANEL_TITLE).text

    def get_article_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NewsPageLocators.ARTICLE_TITLE)
        )
        return self.driver.find_element(*NewsPageLocators.ARTICLE_TITLE).text




