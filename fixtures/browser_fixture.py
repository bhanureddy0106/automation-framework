from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest


@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    options.add_argument("--disable-notifications")

    options.add_argument("--disable-popup-blocking")

    options.add_argument("--disable-infobars")

    options.add_argument("--remote-allow-origins=*")

    driver = webdriver.Remote(

        command_executor="http://localhost:4444/wd/hub",

        options=options
    )

    yield driver

    driver.quit()