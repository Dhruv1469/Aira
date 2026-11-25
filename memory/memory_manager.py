import sqlite3

conn = sqlite3.connect("memory/aira_memory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE,
    value TEXT
)
""")

conn.commit()


def save_memory(key, value):

    cursor.execute(
        """
        INSERT OR REPLACE INTO memories(key, value)
        VALUES (?, ?)
        """,
        (key, value),
    )

    conn.commit()


def get_memory(key):

    cursor.execute(
        """
        SELECT value
        FROM memories
        WHERE key = ?
        """,
        (key,),
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return None
