import time
from selenium import webdriver
from utils.config_loader import load_config
from pages.base_page import BasePage
from pages.notes_page import NotesPage

def test_create_note_ui():
    config = load_config()
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(config["url"])
        # LOGIN
        base = BasePage(driver)
        base.login(config["email"], config["password"])
        # CREATE NOTE
        notes = NotesPage(driver)
        notes.create_note(
            title=f"Automation Note {int(time.time())}",
            description="Created via framework",
            category="Work"
        )
        # FINAL ASSERTION
        assert "Automation Note" in driver.page_source
    finally:
        driver.quit()