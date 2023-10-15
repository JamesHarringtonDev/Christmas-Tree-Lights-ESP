import sqlite3
from sqlite3 import Error
import requests

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):

    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def create_ip(conn):
    sql_create_ip_table = \
    """ CREATE TABLE IF NOT EXISTS ip (
        id integer PRIMARY KEY,
        ip text NOT NULL
    ); """
    try:
        c = conn.cursor()
        c.execute(sql_create_ip_table)
    except Error as e:
        print(e)
    pass


def get_ip():
    ip = get('https://api.ipify.org').content.decode('utf8')

    return ip

def main():
    database = r"ip.db"
    ip = get_ip()
    print(ip)
    # create a database connection
    conn = create_connection(database)
    create_ip(conn)
    with conn:
        # create a new project
        project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        project_id = create_project(conn, project)


if __name__ == '__main__':
    main()