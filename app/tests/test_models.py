from app.domain.models import StockRequest, StockResponse

def test_stock_request_model():
    request = StockRequest(symbol="AAPL", indicator="RSI")
    assert request.symbol == "AAPL"
    assert request.indicator == "RSI"

def test_stock_response_model():
    response = StockResponse(prices=[100.0], indicator_values=[50.0])
    assert response.prices == [100.0]
    assert response.indicator_values == [50.0]
