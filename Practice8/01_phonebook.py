from connect import get_connection


def execute_sql_file(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        sql = file.read()

    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()
    print(f"{filename} выполнен успешно")


def test_upsert():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL insert_or_update_user(%s, %s)", ("Aruzhan", "87011223344"))
    conn.commit()

    print("Upsert procedure works")

    cur.close()
    conn.close()


def test_search():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", ("aru",))
    rows = cur.fetchall()

    print("Search function works:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def test_bulk_insert():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL insert_many_users(%s, %s)",
        (
            ["Tom", "Sara", "Mike", "Lina"],
            ["87012345678", "abc123", "87770001122", "123"]
        )
    )
    conn.commit()

    print("Bulk insert procedure works")

    cur.close()
    conn.close()


def test_pagination():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_with_pagination(%s, %s)", (5, 0))
    rows = cur.fetchall()

    print("Pagination function works:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def test_delete():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", ("Tom",))
    conn.commit()

    print("Delete procedure works")

    cur.close()
    conn.close()


execute_sql_file("Practice8/02_functions.sql")
execute_sql_file("Practice8/03_procedures.sql")

test_upsert()
test_search()
test_bulk_insert()
test_pagination()
test_delete()