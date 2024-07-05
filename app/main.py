import uvicorn
from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router


app = FastAPI(title="Stock Indicator Service")

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # `uvicorn main:app --reload --host 0.0.0.0 --port 8000` after running `python main.py`
