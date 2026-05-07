import time
from utils.config_loader import load_config
from api.notes_api import NotesAPI
from pages.login_page import LoginPage
from pages.notes_page import NotesPage

# UI → API VALIDATION

def test_ui_created_note_should_appear_in_api(driver):
    config = load_config()
    login_page = LoginPage(driver)
    notes_page = NotesPage(driver)
    api = NotesAPI(config)

    title = f"E2E UI API Note {int(time.time())}"
    description = "Created from UI and verified using API"

    # UI LOGIN
    driver.get(config["url"])
    login_page.login(config["email"], config["password"])

    # CREATE NOTE (UI)
    notes_page.create_note(title, description, "Work")

    # WAIT FOR SAVE
    time.sleep(5)

    driver.refresh()

    time.sleep(3)

    # API VALIDATION
    api.login()

    notes = api.get_notes().json()["data"]

    found = False

    for note in notes:
        if note["title"] == title and note["description"] == description:
            found = True
            break

    assert found, "UI created note not found in API"


# UI CREATE → API DELETE → UI VALIDATION

def test_delete_note_using_api_and_verify_in_ui(driver):
    config = load_config()

    login_page = LoginPage(driver)
    notes_page = NotesPage(driver)
    api = NotesAPI(config)

    title = f"E2E Delete Note {int(time.time())}"
    description = "This note will be deleted using API"

    # UI LOGIN
    driver.get(config["url"])

    login_page.login(config["email"], config["password"])

    # CREATE NOTE (UI)
    notes_page.create_note(title, description, "Work")

    # WAIT FOR UI SAVE
    time.sleep(8)

    driver.refresh()

    time.sleep(5)

    # VERIFY CREATED IN UI
    assert not notes_page.is_note_not_visible(title)

    # API LOGIN
    api.login()

    # FIND NOTE IN API
    notes = api.get_notes().json()["data"]

    note_id = None

    for note in notes:
        if note["title"] == title:
            note_id = note["id"]
            break

    assert note_id is not None, "Note not found in API"

    # DELETE VIA API
    delete_response = api.delete_note(note_id)

    assert delete_response.status_code == 200

    # CONFIRM DELETE IN API
    after_notes = api.get_notes().json()["data"]

    assert not any(
        n["id"] == note_id for n in after_notes
    ), "Note still exists in API"

    # WAIT FOR DELETE SYNC
    time.sleep(3)

    # REFRESH UI MULTIPLE TIMES
    driver.refresh()

    time.sleep(2)

    # VERIFY NOTE REMOVED FROM UI
    page = driver.page_source

    assert title not in page