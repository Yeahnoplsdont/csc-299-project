import os
import openai

# Make sure you set your OpenAI API key as an environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

def summarize_task(paragraph):
    response = openai.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "Summarize the following task description into a short phrase."},
            {"role": "user", "content": paragraph}
        ]
    )
    return response.choices[0].message.content.strip()

def main():
    task_descriptions = [
        "Organize kitchen pantry and clean out expired items.",
        "Prepare slides for CSC 299 project presentation."
    ]

    for desc in task_descriptions:
        summary = summarize_task(desc)
        print(f"Original: {desc}")
        print(f"Summary: {summary}\n")

if __name__ == "__main__":
    main()

