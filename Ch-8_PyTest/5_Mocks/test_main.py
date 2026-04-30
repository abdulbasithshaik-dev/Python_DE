import pytest
from main import api_call

def test_api_call(mocker):

    mock_get=mocker.patch("main.requests.get")
    mock_get.return_value.json.return_value={"message":"success"}
    result=api_call("https://api.example.com/data")
    assert result=={"data": {"message":"success"}}