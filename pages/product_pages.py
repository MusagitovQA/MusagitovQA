from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_product_shoes = "//a[@title='OAKMONT TR']"
    select_size = "(//a[@title='8'])[1]"
    add_to_cart = "//button[@class='button-fancy-large add-to-cart ']"
    view_to_cart = "//button[normalize-space()='View Bag']"

    # Getters

    def get_select_product_shoes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_shoes)))

    def get_select_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_view_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.view_to_cart)))

    # Actions

    def click_select_product_shoes(self):
        self.get_select_product_shoes().click()
        print("select product")

    def click_select_size(self):
        self.get_select_size().click()
        print("Click select size")

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Click add to cart")

    def click_view_to_cart(self):
        self.get_view_to_cart().click()
        print("Click view_to_cart")

    # Methods

    def select_shoes(self):
        self.click_select_product_shoes()
        self.click_select_size()
        self.click_add_to_cart()
        self.click_view_to_cart()



