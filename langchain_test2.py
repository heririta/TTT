import os

from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage

SERVER_API = "120.238.149.198"
API_URL = f"http://{SERVER_API}:49040/v1" #8000
API_KEY = "SATU_HATI"
MODEL = "HuggingFaceTB/SmolLM2-360M-Instruct"

model = init_chat_model(
    model=MODEL,
    model_provider="openai",
    base_url=API_URL,
    api_key=API_KEY,
)

system_msg = SystemMessage("Kamu adalah orang indonesia yang mengerti negara dan bangsa indonesia.")
human_msg = HumanMessage(
"Siapa presiden indonesia saat ini."
)
messages = [system_msg, human_msg]

response = model.invoke(messages)
print(response.content)