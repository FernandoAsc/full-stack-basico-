import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS comentarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    autor TEXT NOT NULL,
                    mensagem TEXT NOT NULL
                )""")
    conn.commit()
    conn.close()
