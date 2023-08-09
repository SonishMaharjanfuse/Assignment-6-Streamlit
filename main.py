"""Creating table"""

import sqlite3
import streamlit as st
from database import insert, create_department, create_employee
import pandas as pd

# Initilly uncomment the 2 cell to create the tables
# create_employee()
# create_department()


def employee_table():
    """Insert into the employee table
    """
    st.header("Employee Table")
    empno = st.number_input("Employee number",1,10000)
    ename = st.text_input("Employee name")
    job = st.text_input("Job")
    deptno = st.number_input("Department number", 0, 5)
    if st.button("Add Employee"):
        insert("employee", empno, ename, job, deptno)


def department_table():
    """Insert into the Department table
    """
    st.header("Department Table")
    deptno = st.number_input("Department number",1,5)
    dname = st.text_input("Department name")
    loc = st.text_input("Department location")
    if st.button('Add to department'):
        insert("department", deptno, dname, loc)

def join_table():
    """Join the table employee and department on department number.
    """
    connection = sqlite3.connect("data.db")
    join =  connection.execute(
        """SELECT employee.empno, employee.ename, department.departno, department.dname
            from employee join department on employee.departno = department.departno
        """)
    # join = connection.execute("Select * from employee")
    join = join.fetchall()
    connection.close()

    df = pd.DataFrame(join, columns=["Empno", "Ename", "Departno", "dname"])
    st.header("JOINED TABLE")
    st.dataframe(df)

    

if __name__ == "__main__":
    select = st.sidebar.selectbox("Select page", ['Employee Table', 'Department Table', 'Join Table'])
    if select == 'Employee Table':
        employee_table()

    if select == 'Department Table':
        department_table()
    if select == 'Join Table':
        join_table()
        
        