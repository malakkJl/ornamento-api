from sqlalchemy import create_engine, Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./promotions.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()

class PromotionDB(Base):
    __tablename__ = "promotions"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    discount_percentage = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)
    
print("📦 Création ou vérification de la base promotions.db...")

Base.metadata.create_all(bind=engine)
