from fastapi import FastAPI
from pydantic import BaseModel
from backend.database import init_db, get_connection

app = FastAPI()


# --- Application lifecycle ---
@app.on_event("startup")
def startup():
    """
    Initialize the SQLite database on application startup.
    """
    init_db()


# --- Data models ---
class Query(BaseModel):
    question: str


# --- API endpoints ---
@app.get("/health")
def health():
    """
    Health check endpoint.
    """
    return {"status": "ok"}


@app.post("/query")
def query(q: Query):
    """
    Store the submitted query in the database and return a mock answer.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO queries (question) VALUES (?)",
        (q.question,)
    )
    conn.commit()
    conn.close()

    return {"answer": "mock"}