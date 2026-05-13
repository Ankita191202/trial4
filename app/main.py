from fastapi import FastAPI, Header, HTTPException
from app.routes import router
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

SECRET_TOKEN = os.getenv("SECRET_TOKEN")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API is running not properly"}

@app.get("/secure")
def secure(x_token: str = Header(None)):
    if x_token != SECRET_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": "Access not granted"}
