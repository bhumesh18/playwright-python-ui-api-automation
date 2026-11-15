
from api_tests.utils.response_validator import (
    assert_status_code,
    parse_json_response
)


# Test 1: GET
def test_get_post(api_client):

    response = api_client.get("/posts/1")

    assert_status_code(response, 200)

    data = parse_json_response(response)

    assert data["id"] == 1
    assert data["userId"] == 1
    assert "title" in data


# Test 2: POST
def test_create_post(api_client):

    payload = {
        "title": "API Automation",
        "body": "Testing POST using Playwright",
        "userId": 1
    }

    response = api_client.post("/posts", data=payload)

    assert_status_code(response, 201)

    data = parse_json_response(response)

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


# Test 3: PUT
def test_update_post(api_client):

    payload = {
        "id": 1,
        "title": "Updated using PUT",
        "body": "Complete resource update",
        "userId": 1
    }

    response = api_client.put("/posts/1", data=payload)

    assert_status_code(response, 200)

    data = parse_json_response(response)

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]


# Test 4: PATCH
def test_partial_update(api_client):

    payload = {
        "title": "Updated using PATCH"
    }

    response = api_client.patch("/posts/1", data=payload)

    assert_status_code(response, 200)

    data = parse_json_response(response)

    assert data["title"] == payload["title"]


# Test 5: DELETE
def test_delete_post(api_client):

    response = api_client.delete("/posts/1")

    assert_status_code(response, 200)

    data = parse_json_response(response)

    assert data == {}
