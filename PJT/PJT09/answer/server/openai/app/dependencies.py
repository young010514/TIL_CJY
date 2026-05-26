from dotenv import load_dotenv
import os

load_dotenv(".env")

MODE=os.getenv("MODE")
GMS_KEY=os.getenv("GMS_KEY")
GMS_URL=os.getenv("GMS_URL")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")