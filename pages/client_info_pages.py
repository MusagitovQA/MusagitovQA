from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Client_information(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

    user_mail = "//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_email_emailAddress']"
    first_name = "//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_firstName']"
    last_name = "//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_lastName']"
    street_address = "//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_address1']"
    zip_code = "//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_zip']"
    phone_number = "//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_phone']"
    accept_cookie = "//button[normalize-space()='accept']"
    continue_to_bill = "(//button[normalize-space()='Continue to Billing'])"

    # Getters

    def get_user_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_mail)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_street_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street_address)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_accept_cookie(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_cookie)))

    def get_continue_to_bill(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_to_bill)))

        # Actions

    def input_user_mail(self, user_mail):
        self.get_user_mail().send_keys(user_mail)
        print("Input user mail")

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_street_address(self, street_address):
        self.get_street_address().send_keys(street_address)
        print("Input street address")

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("Input zip code")

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("Input phone number")

    def click_accept_cookie(self):
        self.get_accept_cookie().click()
        print("Click accept_cookie")

    def click_continue_to_bill(self):
        self.get_continue_to_bill().click()
        print("Click continue to bill")

        # Methods

    def input_client_info(self):
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_mail("fogedward@gmail.com")
        self.input_first_name("Edward")
        self.input_last_name("Mus")
        self.input_street_address("371 7th Ave, New York")
        self.input_zip_code("10001")
        self.input_phone_number("212.751.5710")
        self.click_accept_cookie()
        self.click_continue_to_bill()
