import sqlite3
from enum import Enum


class Input(Enum):
    command = 0
    argument = 1


def list_employees(conn):
    cursor = conn.cursor()
    query = "SELECT id, name, position FROM employees;"
    result = cursor.execute(query)
    for row in result:
        print('{} - {} - {}'.format(row['id'], row['name'], row['position']))


def monthly_spending(conn):
    cursor = conn.cursor()
    query = "SELECT SUM(monthly_salary) AS total FROM employees;"
    result = cursor.execute(query)
    result = result.fetchall()
    return result[0]['total']


def yearly_spending(conn):
    cursor = conn.cursor()
    monthly = monthly_spending()
    query = "SELECT SUM(yearly_bonus) AS total FROM employees;"
    result = cursor.execute(query)
    result = result.fetchall()
    bonus = result[0]['total']
    return monthly * 12 + bonus
    

def add_employee(name, monthly_salary, yearly_bonus, position, conn):
    cursor = conn.cursor()
    query = """INSERT INTO employees (name, monthly_salary, yearly_bonus, position)
    VALUES (?, ?, ?, ?);"""
    cursor.execute(query, (name, monthly_salary, yearly_bonus, position))
    conn.commit()

    
def delete_employee(employee_id, conn):
    cursor = conn.cursor()
    query = """DELETE FROM employees WHERE id = ?;"""
    cursor.execute(query, (employee_id))
    conn.commit()


def update_employee(name, monthly_salary, yearly_bonus, position, employee_id, conn):
    cursor = conn.cursor()
    query = """UPDATE employee
SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ?
WHERE id = ?;"""
    cursor.execute(query, (name, monthly_salary,
                           yearly_bonus, position, employee_id))
    conn.commit()


def get_command():
    print('commands: list_employees; monthly_spending; yearly_spending; add_employee; delete_employee <employee_number>; update_employee <employee_number>; exit')
    return input('Enter command> ').split(' ')

    
def get_data():
    employee_data = {}
    employee_data['name'] = input('Name> ')
    employee_data['monthly_salary'] = input('Monhtly salary> ')
    employee_data['yearly_bonus'] = input('Yearlly bonus> ')
    employee_data['position'] = input('Position> ')
    return employee_data

    
def main():
    conn = sqlite3.connect('data.db', timeout=10)
    conn.row_factory = sqlite3.Row

    print('Company Manager')

    while True:

        raw = get_command()
        command = raw[Input['command'].value]
        if command == 'list_employees':
            list_employees(conn)
        elif command == 'monthly_spending':
            monthly_spending(conn)
        elif command == 'yearly_spending':
            yearly_spending(conn)
        elif command == 'add_employee':
            data = get_data()
            add_employee(data['name'], data['monthly_salary'],
                         data['yearly_bonus'], data['position'], conn)
        elif command == 'delete_employee':
            argument = raw[Input['argument'].value]
            delete_employee(argument, conn)
        elif command == 'update_employee':
            argument = raw[Input['argument'].value]
            data = get_data()
            update_employee(data['name'], data['monthly_salary'],
                            data['yearly_bonus'], data['position'], argument, conn)
        elif command == 'exit':
            print('Bye bye!')
            break
        else:
            print('Wrong command!')
    conn.close()

if __name__ == '__main__':
    main()







