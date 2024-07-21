import requests
from requests import Response
import urllib3
urllib3.disable_warnings()
test_url = 'http://127.0.0.1:8000/api/'

def test_delete_204_succesfully(api_browser):
    user_id = 2
    result: Response = requests.delete(test_url+f"users/{user_id}", )
    assert result.status_code == 204