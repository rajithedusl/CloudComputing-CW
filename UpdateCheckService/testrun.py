from fastapi import FastAPI
from fastapi.testclient import TestClient
from github_data_api import app

# app = FastAPI()
client=TestClient(app)


# Testing the / endpoint
def test_ping():
    response = client.get("/")
    assert response.status_code == 200
    assert "DB UPDATE CHECK SERVICE PING SUCCESSFUL : 200" in response.text

# # Testing the /contributors endpoint
# def test_ping1():
#     response = client.get("/contributors")
#     assert response.status_code == 200
