import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

APP_URL = 'http://localhost:4200/'
TRIPS_LISTING_URL = APP_URL + 'trips-listing/'
ADD_TRIP_URL = APP_URL + 'trip_form/'
BASKET_URL = APP_URL + 'basket/'
CONFIGURATION_URL = APP_URL + 'configuration/'


def assert_page_not_found(unit_test, driver):
    page_not_found_wrapper = driver.find_element(By.CLASS_NAME, 'pageNotFoundWrapper')
    page_not_found = page_not_found_wrapper.find_element(By.TAG_NAME, 'h1')

    unit_test.assertEqual("404 - Page not found", page_not_found.text)


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

    # 3
    def test_should_go_back(self):
        # given
        driver = self.driver

        # when
        driver.get(TRIPS_LISTING_URL)
        trip_title = driver.find_element(By.CLASS_NAME, 'name')
        trip_title.click()
        back_button = driver.find_element(By.CLASS_NAME, 'backButton')
        back_button.click()

        # then
        self.assertRegex(driver.current_url, r"\/trips-listing$")

    # 4
    def test_should_guest_not_open_add_trip_page(self):
        # given
        driver = self.driver

        # when
        driver.get(APP_URL)
        driver.get(ADD_TRIP_URL)

        # then
        assert_page_not_found(self, driver)

    # 5
    def test_should_guest_not_open_basket_page(self):
        # given
        driver = self.driver

        # when
        driver.get(APP_URL)
        driver.get(BASKET_URL)

        # then
        assert_page_not_found(self, driver)

    # 6
    def test_should_guest_not_open_configuration_page(self):
        # given
        driver = self.driver

        # when
        driver.get(APP_URL)
        driver.get(CONFIGURATION_URL)

        # then
        assert_page_not_found(self, driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
