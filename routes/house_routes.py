from fastapi import APIRouter,HTTPException,Request,Depends

from schemas.house_schema import HouseFeatures
from controllers.house_controller import predict_price_handler
from lib.rate_limiter import rate_limiter_per_minute

router = APIRouter(prefix="/api")

def get_model(request: Request):
    model = request.app.state.model
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Service unavailable. Please try later"
        )
    return model

@router.get("/", tags=["Root"])
async def health_checker(model = Depends(get_model)):
    return {"success": True, "message": "House Price Prediction API is ready"}

@router.post("/predict",tags=["Prediction"])
@rate_limiter_per_minute()
async def predict_price(request: Request,features: HouseFeatures,model = Depends(get_model)):
    return await predict_price_handler(features,model)