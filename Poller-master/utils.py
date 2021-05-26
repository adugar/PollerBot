import sqlite3
import os

def db():
    conn = sqlite3.connect("web.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS poll(id integer, choices text, creator text, sname text, channelid text)")
    conn.commit()
    conn.close()

def insert(id : int, choices : str, creator : str, sname : str, channelid : str):
    if(check_duplicate(id)):
        return False
    conn = sqlite3.connect("web.db")
    c = conn.cursor()
    c.execute("INSERT INTO poll VALUES(?, ?, ?, ?, ?)", (id, choices, creator, sname, channelid))
    conn.commit()
    conn.close()
    return True


def get_info(id : int):
    conn = sqlite3.connect("web.db")
    c = conn.cursor()
    c.execute("SELECT * FROM poll WHERE id = ?", (id,))
    rows = c.fetchall()
    conn.close()
    return rows[0]

def check_duplicate(id : int):
    conn = sqlite3.connect("web.db")
    c = conn.cursor()
    c.execute("SELECT * FROM poll WHERE id=?", (id,))
    rows = c.fetchall()
    conn.close()
    if rows:
        return True
    else:
        return False

def clear_db():
    os.remove("web.db")

def make_db():
    db()

make_db()