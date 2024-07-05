import pytest
from app.domain.services import StockService
from app.domain.models import StockRequest, StockResponse
from app.infrastructure.tradingview_service import TradingViewService

@pytest.mark.asyncio
async def test_get_stock_data():
    service = StockService(data_service=TradingViewService())
    request = StockRequest(symbol="AAPL", indicator="RSI")
    response = await service.get_stock_data(request)
    assert isinstance(response, StockResponse)
    assert response.prices is not None
