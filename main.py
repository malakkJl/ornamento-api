from fastapi import FastAPI
import database
from routes import router
app = FastAPI()
app.include_router(router)  # 👈 inclure les routes définies dans routes.py

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans ORNAMENTO"}
