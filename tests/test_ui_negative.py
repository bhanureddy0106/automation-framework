import time
import pytest
from selenium import webdriver
from utils.config_loader import load_config
from pages.base_page import BasePage
from pages.notes_page import NotesPage

# TC-NEG-01: Empty Note Validation
def test_ui_negative_empty_note():
    config = load_config()
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(config["url"])
        base = BasePage(driver)
        base.login(config["email"], config["password"])
        notes = NotesPage(driver)
        # OPEN CREATE NOTE MODAL
        notes.create_note("", "", "Work")
        time.sleep(2)
        page = driver.page_source.lower()
        assert (
            "title" in page
            or "required" in page
            or "error" in page
            or "cannot" in page
        )
    finally:
        driver.quit()

# TC-NEG-02: Title Empty
def test_ui_negative_blank_title_only():
    config = load_config()
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(config["url"])
        base = BasePage(driver)
        base.login(config["email"], config["password"])
        notes = NotesPage(driver)
        # EMPTY TITLE
        notes.create_note("", "Only description provided", "Work")
        time.sleep(2)
        page = driver.page_source.lower()
        assert (
            "title" in page
            or "required" in page
            or "error" in page
        )
    finally:
        driver.quit()

# TC-NEG-03: Description Empty
def test_ui_negative_blank_description_only():
    config = load_config()
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(config["url"])
        base = BasePage(driver)
        base.login(config["email"], config["password"])
        notes = NotesPage(driver)

        # EMPTY DESCRIPTION
        notes.create_note("Negative Title", "", "Work")
        time.sleep(2)
        page = driver.page_source.lower()
        assert (
            "description" in page
            or "required" in page
            or "error" in page
        )
    finally:
        driver.quit()
def test_ui_negative_invalid_login():
    config = load_config()
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(config["url"])
        base = BasePage(driver)
        # Invalid Email
        base.login("invalid_email", config["password"])
        time.sleep(2)
        page = driver.page_source.lower()
        assert (
            "email" in page
            or "invalid" in page
            or "error" in page
            or "cannot" in page
        )
        #Reload for next case
        driver.get(config["url"])

        #Invalid Password
        base.login(config["email"], "wrong_password")
        time.sleep(2)
        page = driver.page_source.lower()
        assert (
            "password" in page
            or "invalid" in page
            or "error" in page
            or "cannot" in page
        )
    finally:
        driver.quit()