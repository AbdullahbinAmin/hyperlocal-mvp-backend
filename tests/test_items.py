from src.core.config import settings

def test_create_user(client):
    response = client.post(
        f"{settings.API_V1_STR}/auth/register",
        json={"email": "test@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_login_user(client):
    client.post(
        f"{settings.API_V1_STR}/auth/register",
        json={"email": "test2@example.com", "password": "password123"}
    )
    
    response = client.post(
        f"{settings.API_V1_STR}/auth/login",
        data={"username": "test2@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_create_item(client):
    # Register and login to get token
    client.post(
        f"{settings.API_V1_STR}/auth/register",
        json={"email": "itemowner@example.com", "password": "password123"}
    )
    login_response = client.post(
        f"{settings.API_V1_STR}/auth/login",
        data={"username": "itemowner@example.com", "password": "password123"}
    )
    token = login_response.json()["access_token"]
    
    response = client.post(
        f"{settings.API_V1_STR}/items/",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "My Test Item", "description": "This is a test item"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "My Test Item"
    assert "id" in data
