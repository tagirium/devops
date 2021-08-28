from fastapi import FastAPI
from fastapi.testclient import TestClient
from index import app


def test_read_items():
    with TestClient(app) as client:
        response = client.get("/time")
        assert response.status_code == 200

