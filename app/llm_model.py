import os
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path, override=True)


def get_llm():

    token = os.getenv("HF_TOKEN")

    client = InferenceClient(
        token=token
    )

    return client


MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"