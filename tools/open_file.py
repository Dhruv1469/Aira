import os

def open_file(file_path):

    try:

        os.startfile(file_path)

        return f"Opening file: {file_path}"

    except Exception as e:

        return f"Error opening file {file_path}: {e}"