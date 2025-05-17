from pydantic import BaseModel


class HouseFeatures(BaseModel):
    rooms: int
    square_footage: float
    age: int
    location_score: float


