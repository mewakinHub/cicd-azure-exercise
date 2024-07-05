from abc import ABC, abstractmethod
from app.domain.models import StockRequest, StockResponse

class IStockDataService(ABC):
    """
    Interface for a stock data service that defines the methods required for fetching
    stock data and performing calculations on stock indicators.
    """
    @abstractmethod
    async def fetch_stock_data(self, request: StockRequest) -> StockResponse:
        """
        Fetches stock data based r.
        Must be implemented by any service class inheriting on a specified indicatothis interface.
        """
        pass
