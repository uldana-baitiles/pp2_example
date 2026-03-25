import csv
from connect import get_connection

conn = get_connection()
cur = conn.cursor()

# 1. create table
cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    phone VARCHAR(20)
)
""")
print("Таблица создана")

# 2. insert from csv
with open("Practice7/contacts.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cur.execute(
            "INSERT INTO contacts (username, phone) VALUES (%s, %s)",
            (row["username"], row["phone"])
        )

print("Данные из CSV добавлены")

conn.commit()

# 3. show all contacts
print("Все контакты:")
cur.execute("SELECT * FROM contacts")
rows = cur.fetchall()

for row in rows:
    print(row)

# 4. insert from console
name = input("Введите имя: ")
phone = input("Введите телефон: ")

cur.execute(
    "INSERT INTO contacts (username, phone) VALUES (%s, %s)",
    (name, phone)
)

conn.commit()
print("Контакт добавлен")

# 5. update
old_name = input("Кого изменить: ")
new_phone = input("Новый номер: ")

cur.execute(
    "UPDATE contacts SET phone = %s WHERE username = %s",
    (new_phone, old_name)
)

conn.commit()
print("Контакт обновлен")

# 6. search
search_name = input("Кого ищем: ")

cur.execute(
    "SELECT * FROM contacts WHERE username = %s",
    (search_name,)
)

results = cur.fetchall()

print("Результат поиска:")
for row in results:
    print(row)

# 7. delete
delete_name = input("Кого удалить: ")

cur.execute(
    "DELETE FROM contacts WHERE username = %s",
    (delete_name,)
)

conn.commit()
print("Контакт удален")

# final list
print("Обновленный список:")
cur.execute("SELECT * FROM contacts")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()