from openai import OpenAI

def summarize_task(paragraph: str) -> str:
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "Summarize tasks into short titles."},
            {"role": "user", "content": paragraph}
        ]
    )
    return response.choices[0].message["content"]

def main():
    tasks = [
        "I need to reorganize all of my class notes because they are scattered across different folders. "
        "I want to sort them by course, create summaries, and turn everything into a study guide before finals.",

        "My kitchen pantry is disorganized. I want to remove expired items, group foods by category, "
        "and create a shopping list for missing essentials."
    ]

    for idx, t in enumerate(tasks, 1):
        summary = summarize_task(t)
        print(f"Task {idx} summary: {summary}")

