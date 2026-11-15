# Test 1: Valid Bearer token

def test_bearer_auth_success(auth_api_context):

    token = "demo-token-123"

    response = auth_api_context.get(
        "/bearer",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status == 200

    response_data = response.json()

    assert response_data["authenticated"] is True
    assert response_data["token"] == token

    print("Bearer authentication successful")  

# Test 2: Missing Bearer token

def test_missing_bearer_token(auth_api_context):

    response = auth_api_context.get("/bearer")

    assert response.status == 401

    print("Missing token validation passed") 

# Test 3: Incorrect authorization scheme

def test_invalid_auth_scheme(auth_api_context):

    response = auth_api_context.get(
        "/bearer",
        headers={
            "Authorization": "Basic demo-token-123"
        }
    )

    assert response.status == 401

    print("Invalid authentication scheme validation passed")