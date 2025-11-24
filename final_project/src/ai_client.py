import os
from typing import Optional

# Try to import OpenAI but don't fail hard if missing/quota used
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except Exception:
    OPENAI_AVAILABLE = False

MODEL = "gpt-5-mini"

def summarize_task_text(text: str) -> str:
    """
    Try to call OpenAI. On failure (no key, no quota), return a safe fallback summary.
    """
    if not OPENAI_AVAILABLE or not os.getenv("OPENAI_API_KEY"):
        # deterministic simple fallback so tests are stable:
        return (text.strip()[:60] + "...").replace("\n", " ")
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "Return a 4-word short summary of the user's task."},
                {"role": "user", "content": text},
            ],
            temperature=0.2,
            max_tokens=12,
        )
        return resp.choices[0].message.content.strip()
    except Exception:
        # If anything goes wrong (quota, auth), provide safe deterministic fallback
        return (text.strip()[:60] + "...").replace("\n", " ")
