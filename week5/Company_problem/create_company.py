import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()


def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees
                      (id INTEGER PRIMARY KEY, name TEXT,
                       monthly_salary INTEGER,
                       yearly_bonus INTEGER, position TEXT);""")


def insert_data():
    data = [('Ivan Ivanov', 5000, 10000, 'Software Developer'),
            ('Rado Rado', 500, 0, 'Technical Support Intern'),
            ('Ivo Ivo', 10000, 100000, 'CEO'),
            ('Petar Petrov', 3000, 1000, 'Marketing Manager'),
            ('Maria Georgieva', 8000, 10000, 'COO')]
    for data_tuple in data:
        cursor.execute("""INSERT INTO employees (name, monthly_salary, yearly_bonus, position)
                        VALUES (?,?,?,?);""", data_tuple)
    conn.commit()


create_table()
insert_data()
