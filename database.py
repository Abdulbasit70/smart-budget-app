import sqlite3

def connect_db():
    conn = sqlite3.connect("budget.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        type TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        description TEXT
    )
    """)
    
    conn.commit()
    conn.close()

def delete_transaction(transaction_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    
    conn.commit()
    conn.close()