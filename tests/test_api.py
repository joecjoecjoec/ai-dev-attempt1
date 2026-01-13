import sys
from pathlib import Path

# --- add project root to PYTHONPATH ---
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_query_endpoint():
    response = client.post(
        "/query",
        json={"question": "What is FastAPI?"}
    )
    assert response.status_code == 200
    assert "answer" in response.json()