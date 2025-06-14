from Tests.base_test import BaseTest
from Pages.nasaplus_page import NasaPlusPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# class NasaPlusPageTest(BaseTest):
#     def setUp(self):
#         super().setUp()
#         self.NasaPlus_page = self.home_page.click_nasa_plus()
#
#     def testVideo1Navigation(self):
#         """
#         Checks if the first video in the carousel can be clicked and navigates to the correct URL.
#         """
#         # self.NasaPlus_page.pause_carousel()
#         # vid_url = self.NasaPlus_page.get_video_url()
#         # self.assertIsNotNone(vid_url, "Missing href attribute")
#
#         self.NasaPlus_page.choose_video_1()
#         self.assertEqual(self.driver.current_url, vid_url, "URL mismatch")
#
#         self.NasaPlus_page.click_video_1()
#
#         sleep(5)  # Allow time for the video to load and play
#
#         self.driver.save_screenshot("Tests/screenshots/nasaplus_video1.png")
