import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APP_URL = 'http://localhost:4200/'
TRIPS_LISTING_URL = APP_URL + 'trips-listing/'
ADD_TRIP_URL = APP_URL + 'trip_form/'
BASKET_URL = APP_URL + 'basket/'
CONFIGURATION_URL = APP_URL + 'configuration/'
READER_LOGIN = "reader@reader.com"
WORKER_LOGIN = "worker@worker.com"
ADMIN_LOGIN = "admin@admin.com"


def assert_page_not_found(unit_test, driver):
    page_not_found_wrapper = driver.find_element(By.CLASS_NAME, 'pageNotFoundWrapper')
    page_not_found = page_not_found_wrapper.find_element(By.TAG_NAME, 'h1')

    unit_test.assertEqual("404 - Page not found", page_not_found.text)


def assert_login_successful(unit_test, driver, expected_name):
    # given
    my_account = driver.find_element(By.PARTIAL_LINK_TEXT, "My Account")
    displayed_name = my_account.find_element(By.CLASS_NAME, 'hint')

    # then
    unit_test.assertRegex(driver.current_url, r"\/trips-listing$")
    unit_test.assertEqual(expected_name, displayed_name.text)


def assert_nav_element_present(unit_test, driver, expected_name):
    element = driver.find_element(By.LINK_TEXT, expected_name)
    unit_test.assertEqual(expected_name, element.text)


def go_to_sign_in_page(driver):
    my_account_button = driver.find_element(By.LINK_TEXT, "My Account")
    my_account_button.click()
    account_options = driver.find_element(By.CLASS_NAME, "accountOptions")
    sign_in_button = account_options.find_element(By.CLASS_NAME, "button")
    sign_in_button.click()


def go_to_register_page(driver):
    my_account_button = driver.find_element(By.LINK_TEXT, "My Account")
    my_account_button.click()
    account_options = driver.find_element(By.CLASS_NAME, "accountOptions")
    sign_in_button = account_options.find_element(By.CLASS_NAME, "signUp")
    sign_in_button.click()


def sign_in_user(driver, user_login):
    go_to_sign_in_page(driver)
    id_box = driver.find_element(By.ID, 'email')
    password_box = driver.find_element(By.ID, 'password')
    id_box.send_keys(user_login)
    password_box.send_keys(user_login)
    login_button = driver.find_element(By.CLASS_NAME, 'submitButton')
    login_button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_matches(r"\/trips-listing$"))


def sign_up_user(driver, user_login):
    go_to_register_page(driver)
    id_box = driver.find_element(By.ID, 'email')
    password_box = driver.find_element(By.ID, 'password')
    id_box.send_keys(user_login)
    password_box.send_keys(user_login)
    login_button = driver.find_element(By.CLASS_NAME, 'submitButton')
    login_button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_matches(r"\/trips-listing$"))


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

    # 7
    def test_should_open_sign_in_page(self):
        # given
        driver = self.driver

        # when
        driver.get(APP_URL)
        go_to_sign_in_page(driver)

        # then
        self.assertRegex(driver.current_url, r"\/sign-in$")

    # 8
    def test_should_open_register_page(self):
        # given
        driver = self.driver

        # when
        driver.get(APP_URL)
        go_to_register_page(driver)

        # then
        self.assertRegex(driver.current_url, r"\/sign-up$")

    # 9
    def test_should_login_as_reader(self):
        # given
        driver = self.driver

        # when
        driver.get(APP_URL)
        sign_in_user(driver, READER_LOGIN)

        # then
        assert_login_successful(self, driver, READER_LOGIN)
        assert_nav_element_present(self, driver, 'Basket')

    # 10
    def test_should_login_as_worker(self):
        # given
        driver = self.driver

        # when
        driver.get(APP_URL)
        sign_in_user(driver, WORKER_LOGIN)

        # then
        assert_login_successful(self, driver, WORKER_LOGIN)
        assert_nav_element_present(self, driver, 'Basket')
        assert_nav_element_present(self, driver, 'Add Trip')

    # 11
    def test_should_login_as_admin(self):
        # given
        driver = self.driver

        # when
        driver.get(APP_URL)
        sign_in_user(driver, ADMIN_LOGIN)

        # then
        assert_login_successful(self, driver, ADMIN_LOGIN)
        assert_nav_element_present(self, driver, 'Basket')
        assert_nav_element_present(self, driver, 'Add Trip')
        assert_nav_element_present(self, driver, 'Configuration')

    # 12
    def test_should_register_as_reader(self):
        # given
        driver = self.driver
        new_reader_login = "reader2@reader2.com"

        # when
        driver.get(APP_URL)
        sign_up_user(driver, new_reader_login)

        # then
        assert_login_successful(self, driver, new_reader_login)
        assert_nav_element_present(self, driver, 'Basket')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
