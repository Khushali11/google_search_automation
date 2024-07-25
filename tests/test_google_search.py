import pytest
from selenium import webdriver
from page_objects.google_search_page import GoogleSearchPage
import allure
import time

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    yield driver
    driver.quit()

@allure.feature('Google Search')
@allure.story('Positive Test Case')
def test_search_positive(driver):
    google_search_page = GoogleSearchPage(driver)
    google_search_page.enter_search_query('Selenium Python')
    time.sleep(2)  # Wait for results to load
    assert "Selenium" in google_search_page.get_first_result_title()

@allure.feature('Google Search')
@allure.story('Negative Test Case')
def test_search_negative(driver):
    google_search_page = GoogleSearchPage(driver)
    google_search_page.enter_search_query('asldkjfalksdjfkla')
    time.sleep(2)  # Wait for results to load
    assert "No results found" in google_search_page.get_first_result_title()
