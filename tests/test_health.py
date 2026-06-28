from src.core.config import settings

def test_health_check(client):
    response = client.get(f"{settings.API_V1_STR}/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Hyperlocal MVP API is running"}
