import sqlite3 as sql

conn = sql.connect('phbook.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS phbook(
    id INTEGER PRIMARY KEY,
    fname TEXT,
    lname TEXT,
    number INT,
    status TEXT);
    """)


def write_row(args):
    conn = sql.connect('phbook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO phbook (fname,lname,number,status) VALUES(?,?,?,?);",args)

def del_row(id):
    conn = sql.connect('phbook.db')
    with conn:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM phbook WHERE id = {id}")
    return True

def search_row(data):
    conn = sql.connect('phbook.db')
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM phbook WHERE fname LIKE '%{data}%' OR lname LIKE '%{data}%' OR status LIKE '%{data}%';")
        result = cur.fetchall()
        return result

def read_rows():
    conn = sql.connect('phbook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM phbook;")
        result = cur.fetchall()
        result.insert(0,(tuple(i[0].upper() for i in (cur.execute("select * from phbook limit 1")).description)))
        return result

