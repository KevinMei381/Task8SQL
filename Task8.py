import sqlite3

DATABASE = 'Task8.db'


def print_all_days_desc():
    with sqlite3.connect(DATABASE) as db:
        control = db.cursor()
        # Using triple quotes (""") makes it easy to paste multi-line SQL
        sql = """
        SELECT
            veges.name,
            veges.scientific_name,
            veges.averagedays,
            GROUP_CONCAT(months.month, ', ') AS planting_months
        FROM veges
        JOIN bridge ON veges.vege_id = bridge.vege_id
        JOIN months ON bridge.month_id = months.month_id
        GROUP BY veges.vege_id
        ORDER BY veges.averagedays DESC;
        """
        control.execute(sql)
        results = control.fetchall()
        print(
            f'\n{"Name":<12} '
            f'{"Days to mature":<15} '
            f'{"Ideal planting months":<46}'
            f'{"Scientific Name"}'
        )
        print("-" * 95)
        for row in results:
            print(f'{row[0]:<12} {row[2]:<15} {row[3]:<45} {row[1]:<40} ')


def print_by_month(month_name):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = """
            SELECT veges.name,
            veges.scientific_name,
            veges.averagedays,
                   GROUP_CONCAT(months.month, ', ')
            FROM veges
            JOIN bridge ON veges.vege_id = bridge.vege_id
            JOIN months ON bridge.month_id = months.month_id
            WHERE months.month = ?
            GROUP BY veges.vege_id;
        """
        cursor.execute(sql, (month_name,))
        results = cursor.fetchall()

        if results:
            print(
                f'\n{"Name":<12} '
                f'{"Days to mature":<15} '
                f'{"Ideal planting months":<25}'
                f'{"Scientific Name"}'
            )
            print("-" * 95)
            for row in results:
                print(f'{row[0]:<12} {row[2]:<15} {row[3]:<24} {row[1]:<40} ')


def print_all_by_name():
    with sqlite3.connect(DATABASE) as db:
        control = db.cursor()
        sql = """
        SELECT
            veges.name,
            veges.scientific_name,
            veges.averagedays,
            GROUP_CONCAT(months.month, ', ') AS planting_months
        FROM veges
        JOIN bridge ON veges.vege_id = bridge.vege_id
        JOIN months ON bridge.month_id = months.month_id
        GROUP BY veges.vege_id
        ORDER BY veges.name;
        """
        control.execute(sql)
        results = control.fetchall()
        if results:
            print(
                f'\n{"Name":<12} '
                f'{"Days to mature":<15} '
                f'{"Ideal planting months":<45}'
                f'{"Scientific Name"}'
            )
            print("-" * 95)
            for row in results:
                print(f'{row[0]:<12} {row[2]:<15} {row[3]:<45} {row[1]:<40} ')


def print_by_vege(vege_name):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = """
            SELECT veges.name,
            veges.scientific_name,
            veges.averagedays,
                   GROUP_CONCAT(months.month, ', ')
            FROM veges
            JOIN bridge ON veges.vege_id = bridge.vege_id
            JOIN months ON bridge.month_id = months.month_id
            WHERE veges.name LIKE ?
            GROUP BY veges.vege_id;
        """
        cursor.execute(sql, (f'%{vege_name}%',))
        results = cursor.fetchall()
        if results:
            print(
                f'\n{"Name":<12} '
                f'{"Days to mature":<15} '
                f'{"Ideal planting months":<25}'
                f'{"Scientific Name"}'
            )
            print("-" * 95)
            for row in results:
                print(f'{row[0]:<12} {row[2]:<15} {row[3]:<24} {row[1]:<40} ')
        else:
            print('    Not found')


apple = input(
    """How to print:
    1: Print by how long to mature
    2: Print by name order
    ... OR type a month name
    ... OR by vege name
    > """)

try:
    notapple = int(apple)

    if notapple == 1:
        print_all_days_desc()
    elif notapple == 2:
        print_all_by_name()
except ValueError:
    clean_input = apple.strip().title()
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    if clean_input in months:
        print_by_month(clean_input)
    else:
        print_by_vege(clean_input)
