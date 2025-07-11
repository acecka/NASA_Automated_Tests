from Tests.base_test import BaseTest
from Pages.multi_page import MultiPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class MultiPageTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.multi_page = self.home_page.expand_multimedia()
        self.multi_page = self.home_page.click_multimedia()

    def testGoToNasaPlus(self):
        """ Checks NASA+ navigation menu accuracy"""
        nasa_plus_url = self.multi_page.get_nasa_plus_url()
        self.multi_page.click_nasa_plus()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MultiPageLocators.NASA_PLUS_HEADER))
        self.assertIn("home | nasa+", self.driver.title.lower(), "Failed to navigate to NASA+ page")
        self.assertEqual(self.driver.current_url, nasa_plus_url, "URL mismatch for NASA+ page")

    def testGoToNasaLive(self):
        """ Checks NASA Live navigation menu accuracy and ensures its content is loaded and accurate"""
        nasa_live_url = self.multi_page.get_nasa_live_url()
        self.multi_page.click_nasa_live()
        # wait to process cookies rejection and to let the video play
        sleep(10)
        self.assertEqual(self.driver.current_url, nasa_live_url, "URL mismatch for NASA Live page")
        # ensure the YT account name is "NASA"
        yt_account = self.multi_page.get_yt_account()
        self.assertIn("nasa", yt_account.text.lower(), "YouTube account name is not 'NASA'")

    def testGoToImageGallery(self):
        """ Checks Image Gallery navigation menu accuracy and ensures its content is loaded and accurate"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MultiPageLocators.IMAGE_GALLERY_BUTTON))
        image_gallery_url = self.multi_page.get_image_gallery_url()
        self.multi_page.click_image_gallery()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(MultiPageLocators.IMAGES_HEADER))
        self.assertIn("nasa images", self.driver.title.lower(), "Failed to navigate to Image Gallery page")
        self.assertEqual(self.driver.current_url, image_gallery_url, "URL mismatch for Image Gallery page")
    #
    def testGoToPodcasts(self):
        """ Checks Podcasts navigation menu accuracy and ensures its content is loaded and accurate"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MultiPageLocators.PODCASTS_BUTTON))
        podcasts_url = self.multi_page.get_podcasts_url()
        self.multi_page.click_podcasts()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(MultiPageLocators.PODCASTS_HEADER))
        self.assertIn("podcasts", self.driver.title.lower(), "Failed to navigate to Podcasts page")
        self.assertEqual(self.driver.current_url, podcasts_url, "URL mismatch for Podcasts page")

    def tearDown(self):
        self.driver.quit()
