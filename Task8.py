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
            veges.min_opt_temp,
            veges.max_opt_temp,
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
            f'\n{"Name":<15} '
            f'{"Days to mature":<18} '
            f'{"Ideal planting months":<40} '
            f'{"Optimal temp after germination":<30} '
            f'{"Scientific Name":<30}'
        )
        print("-" * 140)
        for row in results:
            temp_range = f"{row[3]} - {row[4]}°C"
            print(
                f'{row[0]:<15} '
                f'{row[2]:<18} '
                f'{row[5]:<40} '
                f'{temp_range:<30} '
                f'{row[1]:<30}'
            )


def print_by_month(month_name):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = """
            SELECT veges.name,
            veges.scientific_name,
            veges.averagedays,
            veges.min_opt_temp,
            veges.max_opt_temp,
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
                f'\n{"Name":<15} '
                f'{"Days to mature":<18} '
                f'{"Ideal planting months":<40} '
                f'{"Optimal temp after germination":<30} '
                f'{"Scientific Name":<30}'
            )
            print("-" * 140)
            for row in results:
                temp_range = f"{row[3]} - {row[4]}°C"
                print(
                    f'{row[0]:<15} '
                    f'{row[2]:<18} '
                    f'{row[5]:<40} '
                    f'{temp_range:<30} '
                    f'{row[1]:<30}'
                )


def print_all_by_name():
    with sqlite3.connect(DATABASE) as db:
        control = db.cursor()
        sql = """
        SELECT
            veges.name,
            veges.scientific_name,
            veges.averagedays,
            veges.min_opt_temp,
            veges.max_opt_temp,
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
                f'\n{"Name":<15} '
                f'{"Days to mature":<18} '
                f'{"Ideal planting months":<40} '
                f'{"Optimal temp after germination":<30} '
                f'{"Scientific Name":<30}'
            )
        print("-" * 140)
        for row in results:
            temp_range = f"{row[3]} - {row[4]}°C"
            print(
                f'{row[0]:<15} '
                f'{row[2]:<18} '
                f'{row[5]:<50} '
                f'{temp_range:<30} '
                f'{row[1]:<30}'
            )


def print_by_vege(vege_name):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = """
            SELECT veges.name,
            veges.scientific_name,
            veges.averagedays,
            veges.min_opt_temp,
            veges.max_opt_temp,
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
                f'\n{"Name":<15} '
                f'{"Days to mature":<18} '
                f'{"Ideal planting months":<40} '
                f'{"Optimal temp after germination":<30} '
                f'{"Scientific Name":<30}'
            )
            print("-" * 140)
            for row in results:
                temp_range = f"{row[3]} - {row[4]}°C"
                print(
                    f'{row[0]:<15} '
                    f'{row[2]:<18} '
                    f'{row[5]:<40} '
                    f'{temp_range:<30} '
                    f'{row[1]:<30}'
                )
        else:
            print('    Not found')


apple = input(
    """How to print:
    1: Print by how long to mature
    2: Print by name order
    ... OR type a month name
    ... OR by vege name
    > """).strip()
if not apple:
    print('Not found')
else:
    try:
        notapple = int(apple)

        if notapple == 1:
            print_all_days_desc()
        elif notapple == 2:
            print_all_by_name()
        else:
            print('Invalid input')
    except ValueError:
        search = apple.strip().title()
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September",
                  "October", "November", "December"]
        if search in months:
            print_by_month(search)
        else:
            print_by_vege(search)
