import jsonschema
import requests
import urllib3
from requests import Response
from test_api.helper.utils import load_schema

urllib3.disable_warnings()
test_url = 'http://127.0.0.1:8000/api/'

def test_put_update_200_succesfully(api_browser):
    schema = load_schema("put_update.json")
    user_id = 2
    result: Response = requests.put(test_url+f"users/{user_id}")
    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)