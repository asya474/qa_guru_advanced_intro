import jsonschema
import requests
from requests import Response
from test_api.helper.utils import load_schema


def test_put_update_200_succesfully(api_browser):
    schema = load_schema("put_update.json")
    result: Response = requests.put("0.0.0.0", port=8000)
    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)