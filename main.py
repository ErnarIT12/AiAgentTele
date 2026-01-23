from fastapi import FastAPI, APIRouter
from routers.TelegramRouter import router as telegramRouter
app = FastAPI()
app.include_router(telegramRouter)
@app.get("/")
async def root():
    return {"message": "FastAPI is running"}

