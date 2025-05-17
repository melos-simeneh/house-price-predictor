from fastapi import  HTTPException
import numpy as np
from schemas.house_schema import HouseFeatures

async def predict_price_handler(features: HouseFeatures,model):
    input_data = np.array([
        features.rooms,
        features.square_footage,
        features.age,
        features.location_score
    ], dtype=np.float32).reshape(1, -1) 

    try:
        predicted_price = model.predict(input_data)[0]
        return {
            "success":True ,
            "currency": "USD",
            "predicted_price": f"${predicted_price:,.2f}"
        }
    except Exception as e:
        raise HTTPException(
            status_code=422,
            detail=f"Prediction failed: {str(e)}"
        )