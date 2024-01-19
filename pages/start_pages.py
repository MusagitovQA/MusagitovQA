from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Start_page(Base):
    url = 'https://www.fila.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    close_promo = "//span[@class='ui-button-icon ui-icon ui-icon-closethick']"

    # Getters
    def get_close_promo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_promo)))

    # Actions
    def click_close_promo(self):
        self.get_close_promo().click()
        print("Input close_promo")

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_close_promo()
