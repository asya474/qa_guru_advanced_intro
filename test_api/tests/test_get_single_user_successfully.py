import jsonschema
import requests
from requests import Response

from test_api.helper.utils import load_schema


def test_get_single_user_successfully(api_browser):
    schema = load_schema("get_single_user.json")
    result: Response = requests.get(url)
    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)