from app.domain.interfaces import IStockDataService
from app.domain.models import StockRequest, StockResponse

class StockService:
    def __init__(self, data_service: IStockDataService):
        self.data_service = data_service

    async def get_stock_data(self, request: StockRequest) -> StockResponse:
        return await self.data_service.fetch_stock_data(request)
