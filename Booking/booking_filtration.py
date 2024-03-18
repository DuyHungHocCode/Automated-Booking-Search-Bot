from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from lxml import etree

class Booking_Filtration():
    def __init__(self,driver: WebDriver):
        self.driver = driver
        
    def apply_star_rating(self, *star_values):
        star_filtration = self.driver.find_element(By.CSS_SELECTOR, '[data-filters-group="class"]')
        # star_child_elements = star_filtration.find_elements(By.CSS_SELECTOR, 'class:class=1')
        print(5)

        
        for star_value in star_values:
            if star_value == 1:
                star_1 = star_filtration.find_element(By.CSS_SELECTOR,'[name="class=1"]')
                star_1.click()
            if star_value == 2:
                star_2 = star_filtration.find_element(By.CSS_SELECTOR,'[name="class=2"]')
                star_2.click()
            if star_value == 3:
                star_3 = star_filtration.find_element(By.CSS_SELECTOR,'[name="class=3"]')
                star_3.click()
            if star_value == 4:
                star_4 = star_filtration.find_element(By.CSS_SELECTOR,'[name="class=4"]')
                star_4.click()
            if star_value == 5:
                star_5 = star_filtration.find_element(By.CSS_SELECTOR,'[name="class=5"]')
                star_5.click()
            if star_value == 0:
                star_0 = star_filtration.find_element(By.CSS_SELECTOR,'[name="class=0"]')
                star_0.click()
    
    def sort_price_lowest_first(self):
        Sort_by_button = self.driver.find_element(By.CSS_SELECTOR,'[data-testid="sorters-dropdown-trigger"]')
        Sort_by_button.click()
        
        sort_price = self.driver.find_element(By.CSS_SELECTOR, '[data-id="price"]')
        sort_price.click()
        
        