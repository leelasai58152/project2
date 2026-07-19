from pages.first_page import Page
from utils.config import *


def test_page(setup):
    driver=setup
    driver.get(URL)
    page=Page(driver)
    page.open_page()