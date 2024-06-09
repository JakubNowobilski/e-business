import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

APP_URL = 'http://localhost:4200/'
TRIPS_LISTING_URL = APP_URL + 'trips-listing/'


class TravelAgencyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    # 1
    def test_should_open_main_page(self):
        # given
        driver = self.driver

        # when
        driver.get(APP_URL)

        # then
        self.assertEqual("TravelAgency", driver.title)

    # 2
    def test_should_open_trip_details(self):
        # given
        driver = self.driver

        # when
        driver.get(TRIPS_LISTING_URL)
        trip_title = driver.find_element(By.CLASS_NAME, 'name')
        trip_title_text = trip_title.text
        trip_title.click()

        # then
        trip_details_title = driver.find_element(By.CLASS_NAME, 'name')
        self.assertRegex(driver.current_url, r"\/trips-listing\/\d+$")
        self.assertEqual(trip_title_text, trip_details_title.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
