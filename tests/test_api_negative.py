import requests
from utils.config_loader import load_config


def test_api_negative_invalid_token():

    config = load_config()

    headers = {
        "x-auth-token": "INVALID_TOKEN_123"
    }

    response = requests.get(
        f"{config['api_url']}/notes",
        headers=headers
    )

    assert response.status_code in [401, 403]


def test_api_negative_no_token():

    config = load_config()

    response = requests.get(
        f"{config['api_url']}/notes"
    )

    assert response.status_code in [401, 403]

