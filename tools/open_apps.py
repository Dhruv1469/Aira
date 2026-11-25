import subprocess


def open_app(app_name):

    app_name = app_name.lower()

    try:

        if "vscode" in app_name or "vs code" in app_name:

            subprocess.Popen(
                r"C:\Users\LOQ\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            )

            return "Opening VS Code..."

        elif "chrome" in app_name:

            subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

            return "Opening Google Chrome..."

        return f"Sorry, I don't know how to open {app_name}."

    except Exception as e:

        return f"Error opening {app_name}: {e}"
