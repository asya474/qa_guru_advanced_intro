import requests
from requests import Response


def test_delete_204_succesfully(api_browser):
    result: Response = requests.delete(url)
    assert result.status_code == 204