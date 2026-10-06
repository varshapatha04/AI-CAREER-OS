
from core.ollama_client import ask_ollama


def generate_quiz(skill, difficulty="Beginner"):

    prompt = f"""
You are an AI learning mentor.

Create exactly 5 multiple-choice questions about:

SKILL:
{skill}

DIFFICULTY:
{difficulty}

Return ONLY valid JSON.

Use this exact format:

{{
    "questions": [
        {{
            "question": "Question here",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "answer": 0,
            "topic": "Topic tested by this question",
            "explanation": "Short explanation"
        }}
    ]
}}

Rules:

- Create exactly 5 questions.
- Each question must have exactly 4 options.
- The answer must be an integer from 0 to 3.
- Include the topic tested by each question.
- Do not add Markdown.
- Return JSON only.
"""

    result = ask_ollama(prompt)

    return result

