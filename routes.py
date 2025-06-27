from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Promotion, PromotionCreate
from crud import get_all_promotions, get_promotion_by_product, create_promotion
from crud import delete_promotion

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/promotions", response_model=list[Promotion])
def read_promotions(db: Session = Depends(get_db)):
    return get_all_promotions(db)

@router.get("/promotions/{product_id}", response_model=Promotion)
def read_promo(product_id: int, db: Session = Depends(get_db)):
    promo = get_promotion_by_product(db, product_id)
    if not promo:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promo

@router.post("/promotions", response_model=Promotion, status_code=201)
def add_promo(promo: PromotionCreate, db: Session = Depends(get_db)):
    return create_promotion(db, promo)
@router.delete("/promotions/{id}", status_code=204)
def remove_promotion(id: int, db: Session = Depends(get_db)):
    success = delete_promotion(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Promotion non trouvée")