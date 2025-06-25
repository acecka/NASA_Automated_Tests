from Tests.base_test import BaseTest
from Pages.home_page import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VerifyPages(BaseTest):
    def setUp(self):
        super().setUp()

    def testValidPage(self):
        """
        Verifies the page title
        """
        self.assertIn("NASA", self.driver.title, "NASA not found in the title of the page")

    def testGoToNews(self):
        """
        Checks News & Events navigation menu accuracy
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.NEWS_N_EVENTS_LIST))
        self.home_page.expand_news()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.NEWS_N_EVENTS))
        self.home_page.click_news()
        self.assertIn("NASA News", self.driver.title)
        self.assertIn("NASA News", self.driver.find_element(*HomePageLocators.NEWS_PAGE_TITLE).text)

    def testGoToMultimedia(self):
        """
        Checks Multimedia navigation menu accuracy
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.MULTIMEDIA_LIST))
        self.home_page.expand_multimedia()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.MULTIMEDIA))
        self.home_page.click_multimedia()
        self.assertIn("Multimedia - NASA", self.driver.title)
        self.assertIn("Multimedia", self.driver.find_element(*HomePageLocators.MULTIMEDIA_PAGE_TITLE).text)

    def testGoToNASAPlus(self):
        """
        Checks NASA+ navigation menu accuracy
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.NASA_PLUS))
        self.home_page.click_nasa_plus()
        self.assertIn("Home | NASA+", self.driver.title, "Failed to navigate to NASA+ page")

    def testExploreMenuGoToMissions(self):
        """
        Tests the navigation to the Missions page from the Explore menu and verifies the page title and URL.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.EXPLORE_EXPAND))
        self.home_page.driver.find_element(*HomePageLocators.EXPLORE_EXPAND).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.EXPLORE_MISSIONS))
        self.home_page.driver.find_element(*HomePageLocators.EXPLORE_MISSIONS).click()
        missions_url = self.home_page.get_missions_url()
        self.home_page.driver.find_element(*HomePageLocators.EXPLORE_MISSIONS_MAIN).click()
        # Ensures the page title and URL are correct
        self.assertIn("Missions - NASA", self.driver.title, "Failed to navigate to Missions page")
        self.assertEqual(self.driver.current_url, missions_url, "Missions URL mismatch")

    def testExploreMenuGoToUniverse(self):
        """
        Tests the navigation to the Universe page from the Explore menu and verifies the page title and URL.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.EXPLORE_EXPAND))
        self.home_page.driver.find_element(*HomePageLocators.EXPLORE_EXPAND).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.EXPLORE_UNIVERSE))
        self.home_page.driver.find_element(*HomePageLocators.EXPLORE_UNIVERSE).click()
        universe_url = self.home_page.get_universe_url()
        self.home_page.driver.find_element(*HomePageLocators.EXPLORE_UNIVERSE_MAIN).click()
        # Ensures the page title and URL are correct
        self.assertIn("Universe - NASA Science", self.driver.title, "Failed to navigate to Universe page")
        self.assertEqual(self.driver.current_url, universe_url, "Universe URL mismatch")

    def testSearchBoxMarsRover(self):
        """
        Tests the search functionality by entering "Mars Rover" into the search box and verifying the results.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.SEARCH_BOX))
        self.home_page.driver.find_element(*HomePageLocators.SEARCH_BOX).send_keys("Mars Rover")
        self.home_page.driver.find_element(*HomePageLocators.SEARCH_BOX).submit()
        # Main assertion for full phrase to catch most relevant result
        assert "Mars Rover" in self.home_page.driver.find_element(*HomePageLocators.SEARCH_RESULTS1).text, "Mars Rover not found in the first result"
        # Additional less accurate assertion for just "Mars"
        assert "Mars" in self.home_page.driver.find_element(*HomePageLocators.SEARCH_RESULTS_ALL).text, "Mars not found in search results"

    def testSearchBoxVenus(self):
        """
        Tests the search functionality by entering "Venus" into the search box and verifying the results.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.SEARCH_BOX))
        self.home_page.driver.find_element(*HomePageLocators.SEARCH_BOX).send_keys("Venus")
        self.home_page.driver.find_element(*HomePageLocators.SEARCH_BOX).submit()
        # Main assertion for full phrase to catch most relevant result
        assert "Venus" in self.home_page.driver.find_element(*HomePageLocators.SEARCH_RESULTS1).text, "Venus not found in the first result"
        # Additional less accurate assertion for just "Venus"
        assert "Venus" in self.home_page.driver.find_element(*HomePageLocators.SEARCH_RESULTS_ALL).text, "Venus not found in search results"

    def tearDown(self):
        self.driver.quit()
