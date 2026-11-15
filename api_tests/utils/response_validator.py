from playwright.sync_api import APIResponse

#Validate HTTP status code
def assert_status_code(response: APIResponse, expected_status:int):
    assert response.status==expected_status,(
        f"Expected status{expected_status},"
        f"but received {response.status}."
        f"Response body:{response.text()}"
     )

# Validate context type and extract JSON
def parse_json_response(response: APIResponse):
    content_type=response.headers.get("content-type","")
    assert "application/json" in content_type.lower(),(
        f"Expected JSON response but received:{content_type}"
     )

    return response.json()