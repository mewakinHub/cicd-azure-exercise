from pydantic import BaseModel, validator
from typing import List, Optional

class StockRequest(BaseModel):
    symbol: str
    indicator: str

class StockResponse(BaseModel):
    prices: List[float]
    indicator_values: List[Optional[float]]

    @validator('indicator_values', pre=True, each_item=True)
    def ensure_float(cls, v):
        """
        Ensures that all values in indicator_values are floats. Attempts to convert
        strings to floats. If conversion fails, sets the value to None, which represents
        an invalid or unconvertible value without crashing the server.
        """
        try:
            return float(v)
        except (ValueError, TypeError):
            return None


# from pydantic import BaseModel, validator
# from typing import List, Union

# class StockResponse(BaseModel):
#     prices: List[float]
#     indicator_values: List[float]

#     @validator('indicator_values', each_item=True)
#     @classmethod
#     def check_indicator_values(cls, v: Union[float, str]) -> float:
#         """
#         Validates that indicator values are valid floats. Returns the value as float
#         or a default value if conversion fails.

#         Args:
#         v (Union[float, str]): The value to check.

#         Returns:
#         float: The validated float value or 0.0 as a fallback.
#         """
#         try:
#             return float(v)
#         except ValueError:
#             return 0.0  # Consider if you want to return 0.0 or use `None` to indicate invalid inputs
