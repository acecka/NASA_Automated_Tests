from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MultiPageLocators:
    NASA_PLUS_BUTTON = (By.XPATH, '//div/div[4]/div/div/div[1]/a')


class MultimediaPage(BasePage):
    pass
