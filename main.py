from fastapi import FastAPI, APIRouter
from routers.TelegramRouter import router as telegramRouter
app = FastAPI()
telegram_router = APIRouter(tags=["telegram"])
@app.get("/")
async def root():
    return {"message": "Hello World"}