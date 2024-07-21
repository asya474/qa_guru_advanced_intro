import jsonschema
import requests
import urllib3
from requests import Response

from test_api.helper.utils import load_schema

urllib3.disable_warnings()
test_url = 'http://127.0.0.1:8000/api/'

def test_post_create_201_succesfully(api_browser):
    schema = load_schema("post_create.json")
    result: Response = requests.post(test_url+"users")
    assert result.status_code == 201
    jsonschema.validate(result.json(), schema)