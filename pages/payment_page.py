from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    cart_number = "//input[@id='dwfrm_billing_paymentMethods_creditCard_number']"
    secure_cod = "//input[@id='dwfrm_billing_paymentMethods_creditCard_cvn']"
    name_cart = "//input[@id='dwfrm_billing_paymentMethods_creditCard_owner']"

    # Getters

    def get_cart_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_number)))

    def get_secure_cod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.secure_cod)))

    def get_name_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_cart)))

    # Actions

    def input_cart_number(self, cart_number):
        self.get_cart_number().send_keys(cart_number)
        print("Input cart number")

    def input_secure_cod(self, secure_cod):
        self.get_secure_cod().send_keys(secure_cod)
        print("Input secure cod")

    def input_name_cart(self, name_cart):
        self.get_name_cart().send_keys(name_cart)
        print("Input name_cart")
    # Methods

    def payment_info(self):
        self.get_current_url()
        self.input_cart_number("111222333444")
        self.input_secure_cod("444")
        self.input_name_cart("Edward Mus")


