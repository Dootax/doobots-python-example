import pytest
from doobots import Request
from app.main import main

def test_request_get_and_files():
    input_data = {
        "name": "Matheus"
    }
    input_files: list[dict] = [{"base64": "dGVzdA==", "fileName": "teste.txt"}]

    req = Request(input_data, input_files)
    response = main(req)

    assert response.get("greeting") == "Ola, Matheus!"
    assert response.get("fileContent") == "test"