import os
from http.cookiejar import debug
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from agno.tools.duckduckgo import DuckDuckGoTools
from sqlalchemy.sql.functions import session_user
load_dotenv()
def get_agent(session_id : str | None = None ) -> Agent:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key == None:
        raise ValueError("OPENAI_API_KEY is not set")
    return Agent(
        model =OpenAIChat(id = "gpt-3.5- turbo"),
        description= "ты помощник который знает все о сфере финансов",
        db =SqliteDb(db_file="agent.db"),
        session_id = session_id,
        tools = [],
        debug_mode= True,
        markdown = True
    )
