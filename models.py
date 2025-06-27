from pydantic import BaseModel
from datetime import date

class Promotion(BaseModel):
    id: int
    product_id: int
    discount_percentage: float
    start_date: date
    end_date: date

class PromotionCreate(BaseModel):
    product_id: int
    discount_percentage: float
    start_date: date
    end_date: date
