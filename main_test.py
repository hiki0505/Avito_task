from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

SOURCE_URL = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]


def test_get_matrix():
    response = client.get("/get_matrix/", params={"url": SOURCE_URL})
    assert response.status_code == 200
    assert response.json() == TRAVERSAL
