def test_register_program(client):
    response = client.post('/register', json={'repo_url': 'https://github.com/example/hello.git'})
    assert response.status_code == 201
    assert 'Program registered' in response.json['message']