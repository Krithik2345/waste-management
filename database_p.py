import sqlite3
def init_db():
    conn = sqlite3.connect('wasteg_db.sqlite3')

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS garbage(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            waste_type TEXT NOT NULL,
            weight REAL NOT NULL
        )
    ''')
    cursor.execute("DELETE FROM garbage")
    data = [
        ("Hyderabad", "Plastic", 400),
        ("Hyderabad", "Metal", 500),
        ("Hyderabad", "Plastic", 300),

  
        ("Bangalore", "Plastic", 300.5),
        ("Bangalore", "Metal", 600.5),
        ("Bangalore", "Metal", 250),

        ("kerala", "Plastic", 200),
        ("kerala", "Metal", 100),
        ("kerala", "Plastic", 150)
    ]
    cursor.executemany(
        "INSERT INTO garbage(city, waste_type, weight) VALUES(?,?,?)",
        data
    )
    conn.commit()
    cursor.execute("SELECT * FROM garbage")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()
if __name__ == "__main__":
    init_db()