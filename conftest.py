import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    grid_url = os.getenv("GRID_URL", "http://localhost:4444/wd/hub")

    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options
    )

    yield driver
    driver.quit()