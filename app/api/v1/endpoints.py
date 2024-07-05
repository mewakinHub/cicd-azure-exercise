from fastapi import APIRouter, Depends
from app.domain.models import StockRequest, StockResponse
from app.domain.services import StockService
from app.api.v1.dependencies import get_stock_service

router = APIRouter()

@router.post("/stock-data", response_model=StockResponse)
async def stock_data_endpoint(stock_request: StockRequest, service: StockService = Depends(get_stock_service)):
    """
    This service(StockService) got inject w/ dependencies.py w/ constructor named TradingViewService
    """
    return await service.get_stock_data(stock_request)

