import os

IGNORE_DIRS = {"node_modules", ".git", "__pycache__", "venv", ".venv"}

IMPORTANT_EXTENSIONS = {".pdf", ".doc", ".docx", ".txt"}


def find_files(search_term, search_path="D:\\"):

    matches = []

    search_term = search_term.lower()

    try:
        for root, dirs, files in os.walk(search_path):

            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

            for file in files:

                if search_term in file.lower():

                    matches.append(os.path.join(root, file))

    except Exception as e:
        print(f"Error searching for files: {e}")

    matches.sort(key=lambda x: (not x.lower().endswith(tuple(IMPORTANT_EXTENSIONS))))

    return matches
