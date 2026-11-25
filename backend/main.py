import ollama

from tools.open_apps import open_app
from tools.file_search import find_files
from tools.open_file import open_file

last_search_results = []

SYSTEM_PROMPT = """
You are Aira, a personal AI assistant created by Dhruv.

Your name is Aira.

When greeted, respond naturally.

Do not thank people for saying your name.

Keep responses concise and helpful.
"""

print("Aira Online")
print("Type 'exit', 'quit', or 'bye' to quit.\n")

while True:

    user = input("You: ").strip()

    # EXIT
    if user.lower() in ["exit", "quit", "bye"]:

        print("Aira: Goodbye Dhruv!")
        break

    # OPEN FILE FROM LAST SEARCH
    if user.lower().startswith("open "):

        command = user[5:].strip()

        # Open search result number
        if command.isdigit():

            index = int(command) - 1

            if 0 <= index < len(last_search_results):

                result = open_file(last_search_results[index])

                print("Aira:", result)

            else:

                print("Aira: Invalid file number.")

            print()
            continue

        # Open application
        result = open_app(command)

        print("Aira:", result)
        print()

        continue

    # FIND FILES
    if user.lower().startswith("find "):

        query = user[5:].strip()

        results = find_files(query)

        last_search_results = results

        if results:

            print("\nAira: Found these files:\n")

            for i, file in enumerate(results, start=1):
                print(f"{i}. {file}")

        else:

            print("\nAira: No matching files found.")

        print()
        continue

    # AI CHAT
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

        print("Aira: Sorry, I encountered an error:")
        print(str(e))
        print()
