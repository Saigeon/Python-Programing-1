#! /user/bin/env python3
import sqlite3
from contextlib import closing
from business import Item, Shelf
from datetime import date, datetime
conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "fridge_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def create_item(row):
    return Item(row["itemID"], row["itemName"],
                row["itemEnd"], row["itemStart"])

def get_items():
    query = '''SELECT itemID, itemName, itemEnd, itemStart
               FROM contents'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    itemList = Shelf()
    for row in results:
        item = create_item(row)
        itemList.add(item)
    return itemList

def select_item(id):
    query = '''SELECT itemID, itemName, itemStart, itemEnd
               FROM contents
               WHERE itemID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (id))
        row = c.fetchone()
        if row:
            item = create_item(row)
            return item
        else:
            return None

def save_item(item):
    now = datetime.now()
    currentDate = datetime(now.year, now.month, now.day)
    sql = '''INSERT INTO contents
                (itemName, itemEnd, itemStart)
             VALUES
                 (?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (item.itemName, item.itemEnd, currentDate))
    conn.commit()

def delete_item(item):
    sql = '''DELETE
             FROM contents
             WHERE itemID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (item.itemID,))
        conn.commit()

def main():
    pass

if __name__ == "__main__":
    main()
