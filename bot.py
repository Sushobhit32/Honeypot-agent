from groq import Groq
import os


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not set in environment variables")

client = Groq(api_key=GROQ_API_KEY)

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