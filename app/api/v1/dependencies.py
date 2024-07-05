from fastapi import Depends
from app.infrastructure.tradingview_service import TradingViewService
from app.domain.services import StockService

def get_stock_service() -> StockService:
    """
    instantiate TradingViewService class from infrstructure
    """
    return StockService(data_service=TradingViewService())
