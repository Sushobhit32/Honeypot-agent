from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def groq_chat(system_prompt, user_prompt):
    completion = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return completion.choices[0].message.content.strip()
