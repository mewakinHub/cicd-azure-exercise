from tradingview_ta import TA_Handler, Interval # , Exchange
from app.domain.interfaces import IStockDataService
from app.domain.models import StockRequest, StockResponse

class TradingViewService(IStockDataService):
    def __init__(self, exchange: str = "NASDAQ", screener: str = "america"):
        self.exchange = exchange
        self.screener = screener

    async def fetch_stock_data(self, request: StockRequest) -> StockResponse:
        handler = TA_Handler(
            symbol=request.symbol,
            screener=self.screener,
            exchange=self.exchange,
            interval=Interval.INTERVAL_1_WEEK
        )
        analysis = handler.get_analysis()
        price = analysis.indicators['close']  # Assuming 'close' provides the closing price
        indicator_value = analysis.indicators.get(request.indicator, None)
        return StockResponse(prices=[price], indicator_values=[indicator_value if indicator_value else []])
