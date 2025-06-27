from selenium.webdriver import ActionChains

from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class MultiPageLocators:
    NASA_PLUS_BUTTON = (By.XPATH, '//div/div[4]/div/div/div[1]/a')
    NASA_LIVE_BUTTON = (By.XPATH, '//div[5]/div/div/div[1]/a')
    NASA_LIVE_URL = (By.XPATH, '//div/div[5]/div/div/div[1]/a')
    IMAGE_GALLERY_BUTTON = (By.XPATH, '//div[6]/div/div/div[1]/a')
    PODCASTS_BUTTON = (By.XPATH, '//div[7]/div/div/div[1]/a')
    YT_ACCOUNT = (By.XPATH, '//div[1]/ytd-channel-name/div/div/yt-formatted-string/a')
    YT_COOKIES = (By.XPATH, '//c-wiz/div/div/div/div[2]/div[1]')
    YT_REJECT_COOKIES = (By.XPATH, '//div[1]/form[1]/div/div/button')

    IMAGES_HEADER = (By.XPATH, '//div/div[2]/div[2]/div/div[1]/h1')
    PODCASTS_HEADER = (By.XPATH, '//div[3]/h1')
    NASA_LIVE_HEADER = (By.XPATH, '//div/div[1]/div/div/div[1]/div/h3')
    NASA_PLUS_HEADER = (By.XPATH, '//body/div[1]/div[4]/div')


class MultimediaPage(BasePage):
    def click_nasa_plus(self):
        """
        Clicks the NASA+ button on the Multimedia page.
        """
        nasa_plus = self.driver.find_element(*MultiPageLocators.NASA_PLUS_BUTTON)
        # scrolls down to see the button
        self.driver.execute_script("arguments[0].scrollIntoView(true);", nasa_plus)
        ActionChains(self.driver).move_to_element(nasa_plus).perform()
        nasa_plus.click()

    def get_nasa_plus_url(self):
        nasa_plus = self.driver.find_element(*MultiPageLocators.NASA_PLUS_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", nasa_plus)
        ActionChains(self.driver).move_to_element(nasa_plus)
        return nasa_plus.get_attribute("href")

    def click_nasa_live(self):
        """
        Clicks the NASA Live button on the Multimedia page.
        """
        nasa_live = self.driver.find_element(*MultiPageLocators.NASA_LIVE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", nasa_live)
        ActionChains(self.driver).move_to_element(nasa_live).click().perform()
        # wait to load cookie page
        sleep(2)
        self.driver.find_element(*MultiPageLocators.YT_REJECT_COOKIES).click()

    def get_nasa_live_url(self):
        nasa_live = self.driver.find_element(*MultiPageLocators.NASA_LIVE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", nasa_live)
        ActionChains(self.driver).move_to_element(nasa_live)
        return nasa_live.get_attribute("href")

    def get_yt_account(self):
        """
        Returns the YouTube account URL from the Multimedia page.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MultiPageLocators.YT_ACCOUNT))
        return self.driver.find_element(*MultiPageLocators.YT_ACCOUNT)

    def click_image_gallery(self):
        """
        Clicks the Image Gallery button on the Multimedia page.
        """
        image_gallery = self.driver.find_element(*MultiPageLocators.IMAGE_GALLERY_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", image_gallery)
        ActionChains(self.driver).move_to_element(image_gallery).perform()
        image_gallery.click()

    def get_image_gallery_url(self):
        image_gallery = self.driver.find_element(*MultiPageLocators.IMAGE_GALLERY_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", image_gallery)
        ActionChains(self.driver).move_to_element(image_gallery)
        return self.driver.find_element(*MultiPageLocators.IMAGE_GALLERY_BUTTON).get_attribute("href")

    def click_podcasts(self):
        """ Clicks the Podcasts button on the Multimedia page.
        """
        podcasts_button = self.driver.find_element(*MultiPageLocators.PODCASTS_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", podcasts_button)
        ActionChains(self.driver).move_to_element(podcasts_button).perform()
        podcasts_button.click()

    def get_podcasts_url(self):
        podcasts_button = self.driver.find_element(*MultiPageLocators.PODCASTS_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", podcasts_button)
        ActionChains(self.driver).move_to_element(podcasts_button)
        return self.driver.find_element(*MultiPageLocators.PODCASTS_BUTTON).get_attribute("href")
