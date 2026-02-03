from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key="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")

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
