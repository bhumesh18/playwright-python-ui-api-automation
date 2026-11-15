import pytest

@pytest.mark.parametrize(
    "post_id",[1,2,3,10,11]
)

def test_get_post_by_id(api_client,post_id):

    #Send get request using dynamic post ID
    response=api_client.get(f"/posts/{post_id}")

    #Validate status code
    assert response.status==200

    #Extract json response
    response_data=response.json()

    #Validate response fields
    assert response_data["id"]==post_id
    assert isinstance(response_data["title"], str)
    assert isinstance(response_data["body"], str)

    print(f"Post ID {post_id} validated successfully")

# Negative Test : Request a non-existing post

def test_get_non_existing_post(api_client):
    response=api_client.get("/posts/101")

    #Validate the error status
    assert response.status==404

    print("Non-existing post validation passed")

# Query parameter test
def test_query_param(api_client):
    response=api_client.get("/posts", params={"userId":2})

    #Validate status 
    assert response.status==200

    #Extract json response
    response_data=response.json()

    #Verify response fields
    assert isinstance(response_data, list)
    for post in response_data:
        assert post["userId"]==2

    print("Query Parameter test passed")

