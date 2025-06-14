from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class NasaPlusPageLocators:
    PAUSE_BUTTON = (By.XPATH, '//div[3]/div/button')
    VIDEO_THUMBNAIL = (By.XPATH, '//div/div[5]/div/main/div[1]/div[1]/div//div/div/div[2]/a')
    vid = (By.XPATH, '/html/body/div/div[5]/div/main/div[1]/div[1]/div//div/div/div[2]/a')
    VIDEO1 = (By.TAG_NAME, 'video')


class NasaPlusPage(BasePage):
    def pause_carousel(self):
        """
        Clicks the pause button on the carousel.
        """
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(NasaPlusPageLocators.PAUSE_BUTTON))
        self.driver.find_element(*NasaPlusPageLocators.PAUSE_BUTTON).click()
        sleep(2)

    def choose_video_1(self):
        """
        Clicks the first video in the carousel.
        """
        EC.visibility_of_element_located(NasaPlusPageLocators.VIDEO_THUMBNAIL)
        self.driver.find_element(*NasaPlusPageLocators.VIDEO_THUMBNAIL).click()

    def get_video_url(self):
        """
        Returns the URL of the first video in the carousel.
        """
        return self.driver.find_element(*NasaPlusPageLocators.VIDEO_THUMBNAIL).get_attribute("href")

    def click_video_1(self):
        """
        Clicks the playing video to pause.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(NasaPlusPageLocators.VIDEO1))
        self.driver.find_element(*NasaPlusPageLocators.VIDEO1).click()
