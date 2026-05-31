# app/test_hf_api.py

from llm_model import get_llm

client = get_llm()

response = client.chat_completion(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "What is Python?"
        }
    ],
    max_tokens=100
)

print(response.choices[0].message.content)