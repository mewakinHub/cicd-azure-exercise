from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_stock_data_endpoint():
    response = client.post("/api/v1/stock-data", json={"symbol": "AAPL", "indicator": "RSI"})
    assert response.status_code == 200
    data = response.json()
    assert 'prices' in data
    assert 'indicator_values' in data
