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
            f'{"Scientific Name":<40} '
            f'{"Days to mature":<15} '
            f'{"Ideal planting months"}'
        )
        print("-" * 95)
        for row in results:
            print(f'{row[0]:<12} {row[1]:<40} {row[2]:<15} {row[3]}')


def print_by_month(month_name):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = """
            SELECT veges.name, veges.averagedays, veges.scientific_name,
                   GROUP_CONCAT(months.month, ', ')
            FROM veges
            JOIN bridge ON veges.vege_id = bridge.vege_id
            JOIN months ON bridge.month_id = months.month_id
            WHERE months.month LIKE ?
            GROUP BY veges.vege_id;
        """
        cursor.execute(sql, (f'{month_name}%',))
        results = cursor.fetchall()

        if results:
            print(
                 f'\n{"Name":<12} '
                 f'{"Scientific Name":<40} '
                 f'{"Days to mature":<15} '
                 f'{"Ideal planting months"}'
             )
            print("-" * 95)
        for row in results:
            print(f'{row[0]:<12} {row[2]:<40} {row[1]:<15} {row[3]}')


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
        print(
            f'\n{"Name":<12} '
            f'{"Scientific Name":<40} '
            f'{"Days to mature":<15} '
            f'{"Ideal planting months"}'
        )
        print("-" * 95)
        for row in results:
            print(f'{row[0]:<12} {row[1]:<40} {row[2]:<15} {row[3]}')


apple = input(
    """How to print:
    1: Print by maturity (desc)
    2: Print by name order
    ... OR type a month (e.g.May, Apr, Dec) to see what to plant:
    > """)

try:
    choice = int(apple)

    if choice == 1:
        print_all_days_desc()
    elif choice == 2:
        print_all_by_name()
    else:
        print("Invalid number choice.")

except ValueError:
    print_by_month(apple)