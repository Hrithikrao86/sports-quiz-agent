import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_quiz(sport, difficulty, historical_facts, latest_news):

    prompt = f"""
You are a sports quiz generator.

Generate exactly 5 multiple-choice questions.

Return ONLY a valid JSON array.

Do NOT write any explanation.
Do NOT use markdown.
Do NOT wrap the JSON inside ```json.

Format:

[
  {{
    "question": "...",
    "options": [
      "...",
      "...",
      "...",
      "..."
    ],
    "answer": "..."
  }}
]

Sport:
{sport}

Difficulty:
{difficulty}

Historical Facts:
{historical_facts}

Latest News:
{latest_news}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    return json.loads(response.text)