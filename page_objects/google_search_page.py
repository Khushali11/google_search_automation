from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, 'q')

    def enter_search_query(self, query):
        search_box_element = self.driver.find_element(*self.search_box)
        search_box_element.clear()
        search_box_element.send_keys(query)
        search_box_element.send_keys(Keys.RETURN)

    def get_first_result_title(self):
        results = self.driver.find_elements(By.CSS_SELECTOR, 'h3')
        if results:
            return results[0].text
        return "No results found"
