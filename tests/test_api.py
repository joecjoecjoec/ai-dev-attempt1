import sys
from pathlib import Path

# --- ensure project root is on PYTHONPATH (for CI) ---
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from fastapi.testclient import TestClient
from backend.main import app
from backend.database import init_db

# --- initialize database before tests ---
init_db()

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