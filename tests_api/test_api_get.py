def test_api_get_reqres(playwright):
    print('Inside def')
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # not required for ReqRes, but harmless
            "X-Api-Key": "reqres-free-v1"  # not required either
        }
         

    )
    
    response = request.get("https://reqres.in/api/users?page=1")
    assert response.status == 200

    json_data = response.json()
    print(json_data)

    # Validate response structure
    assert "data" in json_data
    assert json_data["data"][3]["first_name"] == "Byron"
    assert json_data["data"][4]["last_name"] == "Edwards"

    request.dispose()
    print("ReqRes Test Completed Successfully")