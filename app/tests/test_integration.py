def test_get_user(app, add_user):
    name = "test"
    last_name = "testing"
    phones_array =  [777777, 666666, 555555]
    user_id = add_user(name, last_name, phones_array)
    client = app.test_client()
    response = client.get(f'http://127.0.0.1:8081/user/{user_id}/')
    user_data = response.json
    assert user_data["user_id"] == user_id
    assert user_data["name"] == name
    assert user_data["last_name"] == last_name
    assert user_data["phones_array"] == phones_array
