import ollama
from tools.open_apps import open_app

SYSTEM_PROMPT = """
You are Aira, a personal AI assistant created by Dhruv.

Your name is Aira.

If someone says:
"Your name is Aira"

reply by acknowledging that your name is Aira.

Never claim your name is anything else.

Keep responses concise and helpful.
"""

print("Aira Online")
print("Type 'exit, quit, or bye' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() in ["exit", "quit", "bye"]:
        print("Aira: Goodbye Dhruv!")
        break

    if user.lower().strip().startswith("open "):
        app = user[5:]

        result = open_app(app)

        print("Aira:", result)
        print()

        continue

    try:
        response = ollama.chat(
            model="deepseek-r1:7b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user},
            ],
        )

        content = response["message"]["content"].strip()
        print("Aira:", content)
        print()
    except Exception as e:
        print("Aira: Sorry, I encountered an error:", str(e))
        print()
