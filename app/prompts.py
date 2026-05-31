INTERVIEW_PROMPT = """
You are an expert technical interviewer.

Based ONLY on the provided context, generate exactly 5 interview questions and answers.

Rules:
1. Use only the provided context.
2. Do not add external knowledge.
3. Generate exactly 5 questions.
4. Follow the format exactly.

Format:

Q1: <question>
A1: <answer>

Q2: <question>
A2: <answer>

Q3: <question>
A3: <answer>

Q4: <question>
A4: <answer>

Q5: <question>
A5: <answer>

Context:
{context}
"""