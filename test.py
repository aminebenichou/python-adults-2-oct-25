import sqlite3


conn = sqlite3.connect("testing.db")

cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS test ( name TEXT, age INTEGER ) ")

conn.commit()

name = "hello"
age = 15
cursor.execute(f"INSERT INTO test (name, age) VALUES ('{name}', {age})")
conn.commit()

cursor.execute("SELECT * FROM test")
data = cursor.fetchall()
print(data)