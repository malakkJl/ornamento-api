from sqlalchemy.orm import Session
from database import PromotionDB
from models import PromotionCreate

def get_all_promotions(db: Session):
    return db.query(PromotionDB).all()

def get_promotion_by_product(db: Session, product_id: int):
    return db.query(PromotionDB).filter(PromotionDB.product_id == product_id).first()

def create_promotion(db: Session, promo: PromotionCreate):
    db_promo = PromotionDB(**promo.dict())
    db.add(db_promo)
    db.commit()
    db.refresh(db_promo)
    return db_promo
def delete_promotion(db: Session, promo_id: int):
    promo = db.query(PromotionDB).filter(PromotionDB.id == promo_id).first()
    if promo:
        db.delete(promo)
        db.commit()
        return True
    return False
