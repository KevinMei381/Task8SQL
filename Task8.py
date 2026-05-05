import sqlite3

DATABASE = 'Task8.db'


def print_all():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Veges;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print nicely
        print('')
        for ID in results:
            print(f'{ID[0]:<2} {ID[1]:<10} {ID[2]:<30} {ID[3]:<8} {ID[4]}')


def print_all_desc():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Veges ORDER BY AverageDays DESC;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print nicely
        print('')
        for ID in results:
            print(f'{ID[0]:<2} {ID[1]:<10} {ID[2]:<30} {ID[3]:<8} {ID[4]}')


apple = input('1 or 2?')
try:
    int(apple)
    if apple == '1':
        print_all_desc()
    elif apple == '2':
        print_all()
except ValueError:
    print('no')
