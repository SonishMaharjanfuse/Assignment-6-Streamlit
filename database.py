"""Create Database"""
import sqlite3


def create_employee():
    """ Creating the table for employee
    """
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS employee(
                    empno INT PRIMARY KEY,
                    ename VARCHAR(25),
                    job VARCHAR(20),
                    departno INT,
                    FOREIGN KEY (departno) REFERENCES department(departno)
                    )"""
    )
    connection.commit()
    connection.close()


def create_department():
    """Creating the table for department.
    """
    connection = sqlite3.connect("data.db")
    connection.cursor()
    connection.execute(
        """CREATE TABLE department(
                    departno INT PRIMARY KEY,
                    dname VARCHAR(25),
                    loc VARCHAR(20)
                    )
                    """
    )
    connection.commit()
    connection.close()


def insert(table_name, *args):
    """" Function to insert into the table
    """
    connection = sqlite3.connect("data.db")
    connection.cursor()
    connection.execute(
        f"""
INSERT INTO {table_name} VALUES"""+str(tuple(arg for arg in args))
    )
    connection.commit()
    connection.close()


def drop(table_name):
    """Dropping the table"""
    connection = sqlite3.connect('data.db')
    connection.execute(f"""DROP TABLE {table_name}""")
