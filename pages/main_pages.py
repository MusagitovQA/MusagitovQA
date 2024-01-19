from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_category_men = "//a[@aria-controls='subnav-men']"
    select_shoes = "//a[@class='cat-refinement '][3]"
    select_color = "//dt[normalize-space()='Color']"
    select_color_shoes = "//a[@id='swatch-red']"

    # Getters

    def get_select_category_men(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_category_men)))

    def get_select_shoes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_shoes)))

    def get_select_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_color)))

    def get_select_color_shoes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_color_shoes)))

    # Actions
    def click_select_category_men(self):
        self.get_select_category_men().click()
        print("Click select_category_men")

    def click_select_shoes(self):
        self.get_select_shoes().click()
        print("Click select_shoes")

    def click_select_color(self):
        self.get_select_color().click()
        print("Click select_color")

    def click_select_color_shoes(self):
        self.get_select_color_shoes().click()
        print("Click select_color_shoes")

    # Methods

    def select_product(self):
        self.get_current_url()
        self.click_select_category_men()
        self.click_select_shoes()
        self.click_select_color()
        self.click_select_color_shoes()


