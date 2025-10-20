import sqlite3


conn = sqlite3.connect('tiktok.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM tiktok_data LIMIT 5;")

print(cursor.fetchall())
cursor.execute("SELECT COUNT(*) FROM tiktok_data;")

print(cursor.fetchall())
conn.close()
