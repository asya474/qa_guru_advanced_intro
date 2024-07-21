import jsonschema
import requests
import urllib3
from requests import Response
from test_api.helper.utils import load_schema

urllib3.disable_warnings()
test_url = 'http://127.0.0.1:8000/api/'

def test_get_single_user_successfully(api_browser):
    schema = load_schema("get_single_user.json")
    user_id = 2
    result: Response = requests.get(test_url+f"users/{user_id}")
    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)