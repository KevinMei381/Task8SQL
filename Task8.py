import sqlite3

DATABASE = 'Task8.db'


def print_all():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Veges;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print nicely
        for ID in results:
            print(f'{ID[0]} {ID[1]} {ID[2]} {ID[3]} {ID[4]}')


print_all()
