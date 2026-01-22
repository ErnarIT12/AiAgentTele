from fastapi import APIRouter, Request, BackgroundTasks
import httpx
import os
from dotenv import load_dotenv
from service.agent_service import get_agent
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
router = APIRouter(tags=["TelegramRouter"], prefix="/api")

@router.post("/telegram")
async def create_telegram_router(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_text = data["message"].get("text", "")
        background_tasks.add_task(process_telegram_message, chat_id, user_text)

    return {"status": "ok"}

async def process_telegram_message(chat_id: int, text: str):
    if not text:
        return

    agent = get_agent(session_id=str(chat_id))
    agent_response = agent.run(text)

    telegram_api_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    async with httpx.AsyncClient() as client:
        await client.post(telegram_api_url, json={
            "chat_id": chat_id,
            "text": agent_response.content,
            "parse_mode": "Markdown"
            })