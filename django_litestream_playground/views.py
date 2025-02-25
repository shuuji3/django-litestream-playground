import datetime
import sqlite3
from contextlib import closing

from django.http import HttpRequest
from django.shortcuts import render


def home(request: HttpRequest):
    now = datetime.datetime.now()
    tables = get_all_table_names()
    index_tables = get_all_index_table_names()
    return render(request, "home.html", {"now": now, "tables": tables, "index_tables": index_tables})


def get_all_table_names() -> [str]:
    """Gets a list of all table names."""
    try:
        with closing(sqlite3.connect('db.sqlite3')) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                table_names = [row[0] for row in cursor.fetchall()]
                return table_names
    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
        return []

def get_all_index_table_names() -> [str]:
    """Gets a list of all index table names."""
    try:
        with closing(sqlite3.connect('db.sqlite3')) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='index';")
                index_table_names = [row[0] for row in cursor.fetchall()]
                return index_table_names
    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
        return []
