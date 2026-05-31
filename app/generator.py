from app.llm_model import get_llm, MODEL_NAME
from app.prompts import INTERVIEW_PROMPT


def generate_interview_questions(context):

    client = get_llm()

    prompt = INTERVIEW_PROMPT.format(
        context=context
    )

    response = client.chat_completion(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1000
    )

    return response.choices[0].message.content