import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
    service = Service()  # Selenium Manager handles driver
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    yield driver

    driver.quit()