from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def get_admin_token() -> str:
    response = client.post(
        "/api/auth/login",
        json={"email": "admin@assistencia.com", "senha": "admin123"},
    )
    assert response.status_code == 200
    return response.json()["token"]


def test_manual_backup_requires_admin():
    response = client.post("/api/backup/manual")
    assert response.status_code == 401


def test_manual_backup_creates_backup_file():
    token = get_admin_token()
    response = client.post(
        "/api/backup/manual",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["success"] is True
    assert payload["file_name"].endswith(".sqlite")


def test_restore_backup():
    token = get_admin_token()
    backup_response = client.post(
        "/api/backup/manual",
        headers={"Authorization": f"Bearer {token}"},
    )
    backup_id = backup_response.json()["backup_id"]

    restore_response = client.post(
        f"/api/backup/restore/{backup_id}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert restore_response.status_code == 200
    assert restore_response.json()["success"] is True