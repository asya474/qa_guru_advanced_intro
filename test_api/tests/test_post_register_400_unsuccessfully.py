import jsonschema
import requests
from requests import Response

from test_api.helper.utils import load_schema


def test_post_register_400_unsuccessfully(api_browser):
    url = "https://reqres.in/api/register"
    schema = load_schema("post_400.json")

    result: Response = requests.post(url)

    assert result.status_code == 400
    jsonschema.validate(result.json(), schema)