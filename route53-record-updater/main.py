import sqlite3
from sqlite3 import Error
import requests
import os.path
import os
from datetime import date


ENVS = ['USERNAME']


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_ip(conn, ip):
    today = date.today()
    print(today)
    data = [ip, str(today), "fil"]
    print(data)
    sql = "INSERT INTO ip(ip, date, name) VALUES(?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid


def get_ip():
    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    return ip


def db_exists():
    return os.path.isfile("ip.db")


def create_db():
    # TODO: do the db creation stuff
    sql_create_ip_table = """ CREATE TABLE IF NOT EXISTS ip (
                                         id integer PRIMARY KEY,
                                         ip TEXT NOT NULL,
                                         date TEXT NOT NULL,
                                         name text NOT NULL
                                     ); """

    db = r"ip.db"
    conn = create_connection(db)
    c = conn.cursor()
    try:
        c.execute(sql_create_ip_table)
    except Error as e:
        return False

    return True


def get_env(name):
    name = f"RCT_{name}"
    if name in os.environ:
        return os.environ[name]
    else:
        return False


def main():

    username = get_env('USERNAME')
    print(username)
    if not username:
        raise Exception("RCT_USERNAME env variable  not found")

    database = r"ip.db"
    if not db_exists():
        status = create_db()
        if not status:
            print("db creation fail, oh no")

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        ip = get_ip()
        ip_id = create_ip(conn, ip)
        print(ip_id)


if __name__ == '__main__':
    main()