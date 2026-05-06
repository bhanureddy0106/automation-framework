from selenium import webdriver
from pages.login_page import LoginPage
from utils.config_loader import load_config


def test_login():
    config = load_config()

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(config["url"])

    login = LoginPage(driver)
    login.login(config["email"], config["password"])

    assert "notes" in driver.current_url

    driver.quit()


def test_successful_ui_login(driver):
    config = load_config()

    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.login(config["email"], config["password"])

    page_text = driver.page_source.lower()

    assert "notes" in driver.current_url.lower() or "my notes" in page_text or "add note" in page_text