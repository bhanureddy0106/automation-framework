import time
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config_loader import load_config
from utils.performance_logger import log_performance  
from utils.agentic_utils import measure_time

# SIMPLE LOGIN TEST
def test_login():
    config = load_config()
    driver = webdriver.Chrome()
    driver.maximize_window()
    start = time.time()   #START TIMER
    driver.get(config["url"])
    login = LoginPage(driver)
    measure_time(lambda: login.login(config["email"], config["password"]))
    end = time.time()     #END TIMER
    duration = end - start
    print(f"[UI LOGIN TIME]: {duration}")
    log_performance("UI_LOGIN_TIME", duration)   #TREND LOG
    assert "notes" in driver.current_url
    driver.quit()

# UI LOGIN 

def test_successful_ui_login(driver):
    config = load_config()
    login_page = LoginPage(driver)
    start = time.time()   #START TIMER
    login_page.open_login_page()
    measure_time(lambda: login_page.login(config["email"], config["password"]))
    end = time.time()     #END TIMER
    duration = end - start
    print(f"[UI LOGIN FLOW TIME]: {duration}")
    log_performance("UI_LOGIN_FLOW", duration)   #TREND LOG
    page_text = driver.page_source.lower()
    assert (
        "notes" in driver.current_url.lower()
        or "my notes" in page_text
        or "add note" in page_text
    )