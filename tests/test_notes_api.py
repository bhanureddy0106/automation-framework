import time
from api.notes_api import NotesAPI
from utils.config_loader import load_config
from utils.performance_logger import log_performance  

# API LOGIN + GET NOTES
def test_api_login_and_get_notes():
    config = load_config()
    api = NotesAPI(config)
    start = time.time()   #PERFORMANCE START
    token = api.login()
    assert token is not None
    assert len(token) > 0
    response = api.get_notes()
    end = time.time()     #PERFORMANCE END
    duration = end - start
    print(f"[API LOGIN + GET NOTES TIME]: {duration}")
    log_performance("API_LOGIN_GET_NOTES", duration)   #TREND LOG
    assert response.status_code == 200
    assert response.json()["success"] is True

# API PERFORMANCE TEST
def test_api_response_time_less_than_2_seconds():
    config = load_config()
    api = NotesAPI(config)
    api.login()
    start = time.time()   #START
    response = api.get_notes()
    end = time.time()     #END
    response_time = end - start
    print(f"[API RESPONSE TIME]: {response_time}")
    log_performance("API_RESPONSE_TIME", response_time)   #TREND LOG
    assert response.status_code == 200
    assert response_time < 2

# CREATE → UPDATE → DELETE
def test_api_create_update_and_delete_note():
    config = load_config()
    api = NotesAPI(config)
    api.login()
    unique_title = f"API Automation Note {int(time.time())}"
    description = "Created using API automation"
    start = time.time()   #START

    # CREATE
    create_response = api.create_note(unique_title, description, "Work")
    assert create_response.status_code == 200
    note_id = create_response.json()["data"]["id"]

    # UPDATE
    updated_title = f"Updated {unique_title}"
    updated_description = "Updated using API automation"
    update_response = api.update_note(
        note_id,
        updated_title,
        updated_description,
        "Work",
        completed=False
    )
    assert update_response.status_code == 200
    assert update_response.json()["data"]["title"] == updated_title

    # DELETE
    delete_response = api.delete_note(note_id)
    end = time.time()   #END
    duration = end - start
    print(f"[API CRUD FLOW TIME]: {duration}")
    log_performance("API_CRUD_FLOW", duration)   #TREND LOG
    assert delete_response.status_code == 200