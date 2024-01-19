import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.cart_pages import Cart_page
from pages.client_info_pages import Client_information
from pages.finish_page import Finish_page
from pages.main_pages import Main_page
from pages.payment_page import Payment_page
from pages.product_pages import Product_page
from pages.start_pages import Start_page


def test_buy_product():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start test")

    login = Start_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product()

    pp = Product_page(driver)
    pp.select_shoes()

    cp = Cart_page(driver)
    cp.click_checkout()

    cip = Client_information(driver)
    cip.input_client_info()

    p = Payment_page(driver)
    p.payment_info()

    f = Finish_page(driver)
    f.finish()

    print("Finish Test")
    time.sleep(10)
    driver.quit()
