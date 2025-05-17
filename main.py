from fastapi import FastAPI, HTTPException
import joblib
import os
from contextlib import asynccontextmanager
import lib.exception_handlers as exception_handlers
from fastapi.exceptions import RequestValidationError
from slowapi.errors import RateLimitExceeded

from routes import house_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    MODEL_FILENAME = 'data/house_price_model.pkl'
    MODEL_PATH = os.path.join(os.path.dirname(__file__), MODEL_FILENAME)
    
    if not os.path.exists(MODEL_PATH):
        raise RuntimeError(f"Model file '{MODEL_FILENAME}' not found at '{MODEL_PATH}'")
    
    try:
        model = joblib.load(MODEL_PATH)
        app.state.model = model
        yield
    finally:
        pass

app = FastAPI(
    title="House Prediction API",
    description="Predict house prices based on features like size, age, and location.",
    lifespan=lifespan
)

app.add_exception_handler(RateLimitExceeded,exception_handlers.rate_limit_exceeded_handler)
app.add_exception_handler(RequestValidationError,exception_handlers.validation_exception_handler)
app.add_exception_handler(HTTPException,exception_handlers.http_exception_handler)
app.add_exception_handler(Exception,exception_handlers.general_exception_handler)


app.include_router(house_routes.router)