import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Read CSV
df = pd.read_csv("employee.csv")

# =========================
# DISPLAY DATA AS TABLE
# =========================
print("\nEMPLOYEE DATASET\n")
print(tabulate(df, headers='keys', tablefmt='grid'))

# =========================
# BASIC ANALYSIS
# =========================
print("\nSUMMARY STATISTICS\n")
print(tabulate(df.describe(), headers='keys', tablefmt='grid'))

print("\nDEPARTMENT WISE EMPLOYEE COUNT\n")
dept_count = df['Department'].value_counts()
print(tabulate(dept_count.reset_index(),
               headers=['Department', 'Count'],
               tablefmt='grid',
               showindex=False))

print("\nAVERAGE SALARY BY DEPARTMENT\n")
avg_salary = df.groupby('Department')['Salary'].mean()
print(tabulate(avg_salary.reset_index(),
               headers=['Department', 'Average Salary'],
               tablefmt='grid',
               showindex=False))

# =========================
# ALL GRAPHS IN ONE WINDOW
# =========================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Department Count
dept_count.plot(
    kind='bar',
    ax=axes[0, 0],
    title='Department Wise Employee Count'
)
axes[0, 0].set_xlabel('Department')
axes[0, 0].set_ylabel('Employees')

# 2. Salary Distribution
axes[0, 1].hist(
    df['Salary'],
    bins=5
)
axes[0, 1].set_title('Salary Distribution')
axes[0, 1].set_xlabel('Salary')
axes[0, 1].set_ylabel('Frequency')

# 3. Salary vs Experience
axes[1, 0].scatter(
    df['Experience_Years'],
    df['Salary']
)
axes[1, 0].set_title('Salary vs Experience')
axes[1, 0].set_xlabel('Experience (Years)')
axes[1, 0].set_ylabel('Salary')

# 4. Department Salary Average
avg_salary.plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=axes[1, 1]
)
axes[1, 1].set_title('Department Salary Share')
axes[1, 1].set_ylabel('')

plt.tight_layout()
plt.show()
