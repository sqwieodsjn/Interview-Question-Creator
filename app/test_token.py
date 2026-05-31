from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(__file__).parent.parent / ".env"

print("ENV FILE:", env_path)

loaded = load_dotenv(env_path, override=True)

print("LOADED:", loaded)

token = os.getenv("HF_TOKEN")

print("TOKEN:", token)
print("LENGTH:", len(token) if token else 0)