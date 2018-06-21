import sqlite3

def connect():
    conn = sqlite3.connect("clients.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS clients " + 
                "(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT," +
                " last_name TEXT, gender TEXT, address TEXT, city TEXT," +
                " province TEXT, phone_number INTEGER, zip_code TEXT, balance REAL)")
    conn.commit()
    conn.close()

def insert_basic(first_name, last_name, gender):
    conn = sqlite3.connect("clients.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO clients (id, first_name, last_name, gender) VALUES (NULL, ?, ?, ?)", (first_name, last_name, gender))
    conn.commit()
    conn.close()
    
def view():
    conn = sqlite3.connect("clients.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(firstname_arg = "", lastname_arg = "", gender_arg = ""):
    conn = sqlite3.connect("clients.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients WHERE first_name = ? OR last_name = ?  OR gender = ? ", (firstname_arg, lastname_arg, gender_arg))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id_key):
    conn = sqlite3.connect("clients.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM clients WHERE id = ?", (id_key,))
    conn.commit()
    conn.close()

def update_basic(id_key, firstname_arg, lastname_arg, gender_arg):
    conn = sqlite3.connect("clients.db")
    cur = conn.cursor()
    cur.execute("UPDATE clients SET first_name = ?, last_name = ?, gender = ? WHERE id = ?", (firstname_arg, lastname_arg, gender_arg, id_key))
    conn.commit()
    conn.close()

def update_personal(id_key, address_arg, city_arg, province_arg, phonenumber_arg, zipcode_arg):
    conn = sqlite3.connect("clients.db")
    cur = conn.cursor()
    cur.execute("UPDATE clients SET address = ?, city = ?, province = ?, phone_number = ?, zip_code = ? WHERE id = ?", (address_arg, city_arg, province_arg, phonenumber_arg, zipcode_arg, id_key))
    conn.commit()
    conn.close()

def update_balance(id_key, balance_arg):
    conn = sqlite3.connect("clients.db")
    cur = conn.cursor()
    cur.execute("UPDATE clients SET balance = ? WHERE id = ?", (balance_arg, id_key))
    conn.commit()
    conn.close()
    
def select_client(id_key):
    conn = sqlite3.connect("clients.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients WHERE id = ?", (id_key,))
    row = cur.fetchall()
    conn.close()
    return row

def login_client(firstname_arg, lastname_arg):
    conn = sqlite3.connect("clients.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients WHERE first_name = ? AND last_name = ?", (firstname_arg, lastname_arg))
    row = cur.fetchall()
    conn.close()
    return row

connect()
