import requests
from requests import Response


def test_delete_204_succesfully(api_browser):
    result: Response = requests.delete("0.0.0.0", port=8000)
    assert result.status_code == 204