import pytest
from selenium import webdriver
from helper import OrderDataHelper
from URL import MAIN_URL

@pytest.fixture
def driver():
    driver=webdriver.Firefox()
    driver.maximize_window()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()

@pytest.fixture
def data():
    return OrderDataHelper.generate_order_data()