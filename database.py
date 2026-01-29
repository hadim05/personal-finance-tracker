mport sqlite3

def connect_db():
    return sqlite3.connect("finance.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    
def add_transaction(t_type, category, amount, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (type, category, amount, date) VALUES (?, ?, ?, ?)",
        (t_type, category, amount, date)
    )
    conn.commit()
    conn.close()
    
def get_transactions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    data = cursor.fetchall()
    conn.close()
    return data
    
 def get_monthly_summary(month):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT type, SUM(amount)
        FROM transactions
        WHERE date LIKE ?
        GROUP BY type
    """, (f"{month}%",))

    results = cursor.fetchall()
    conn.close()
    return results
