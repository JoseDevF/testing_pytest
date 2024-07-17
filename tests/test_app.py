# Prueba de caja negra, simulando un timeout
# no controlamos la API (en teoría)
# No tienes acceso al código
# region parte 1

# from unittest.mock import Mock
# import requests
# from requests.exceptions import Timeout
#
#
# requests = Mock()
#
#
# def test_connection():
#     requests.get.side_effect = Timeout
#     response = requests.get("http://127.0.0.1:8000")
#     print("\n\n", response.text)


# endregion

# Pruebas de caja blanca
# Este ejercicio se realiza teniendo httpx


from fastapi.testclient import TestClient
from fastapi.exceptions import HTTPException
from web.main import app
from unittest.mock import patch


client = TestClient(app)


def test_connection():
    with patch("web.main.time") as mock:
        mock.sleep.side_effect = HTTPException(status_code=504)
        response = client.get("/timeout")
        print("\n\n", response.text)



import requests
from unittest.mock import Mock


def get_weather(api_url):
    response = requests.get(api_url)
    return response.json()


def test_get_weather():
    requests.get = Mock()
    requests.get.return_value.json.return_value = {"weather": "sunny"}

    result = get_weather("http://fakeurl.com")
    assert result == {"weather": "sunny"}