# 176. Second Highest Salary
'''
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
'''

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique = employee['salary'].drop_duplicates()

    second = unique.nlargest(2).iloc[-1] if len(unique) >= 2 else None
    
    if second is None:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    return pd.DataFrame({'SecondHighestSalary': [second]})