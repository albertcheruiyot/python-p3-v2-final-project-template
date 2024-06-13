import os
import sqlite3
from helpers import execute_query, fetch_all, fetch_one

DB_FILE = 'employee_management.db'

class Department:
    @staticmethod
    def create_table():
        execute_query('''
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')

    @staticmethod
    def create(name):
        execute_query('INSERT INTO departments (name) VALUES (?)', (name,))
        department_id = fetch_one('SELECT last_insert_rowid()')[0]
        return department_id

    @staticmethod
    def delete(department_id):
        execute_query('DELETE FROM departments WHERE id = ?', (department_id,))

    @staticmethod
    def get_all():
        return fetch_all('SELECT * FROM departments')

class Employee:
    @staticmethod
    def create_table():
        execute_query('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                salary REAL NOT NULL,
                department_id INTEGER,
                FOREIGN KEY (department_id) REFERENCES departments(id)
            )
        ''')

    @staticmethod
    def create(name, age, salary, department_id):
        execute_query('INSERT INTO employees (name, age, salary, department_id) VALUES (?, ?, ?, ?)', (name, age, salary, department_id))
        employee_id = fetch_one('SELECT last_insert_rowid()')[0]
        return employee_id

    @staticmethod
    def delete(employee_id):
        execute_query('DELETE FROM employees WHERE id = ?', (employee_id,))

    @staticmethod
    def get_all():
        return fetch_all('SELECT * FROM employees')


    @staticmethod
    def get_by_department_id(department_id):
        return fetch_all('SELECT * FROM employees WHERE department_id = ?', (department_id,))


# Create database and tables if they don't exist
if not os.path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    conn.close()

Department.create_table()
Employee.create_table()
