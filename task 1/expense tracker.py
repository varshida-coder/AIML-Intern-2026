import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

budgets = {
    "Food": 2000,
    "Snacks": 500,
    "Travel": 1000,
    "Personal": 500,
    "Medicine": 300,
    "Outing": 500,
    "Birthday Gift": 500,
    "Miscellaneous": 500,
    "Semester Fees": 5000
}

expenses = []

def refresh():
    tree.delete(*tree.get_children())
    totals = {k: 0 for k in budgets}

    for e in expenses:
        tree.insert("", "end", values=e)
        totals[e[1]] += float(e[3])

    report = ""
    total_budget = sum(budgets.values())
    total_spent = sum(totals.values())

    for cat in budgets:
        spent = totals[cat]
        remain = budgets[cat] - spent
        report += f"{cat}: Budget ₹{budgets[cat]} | Spent ₹{spent:.0f} | Remaining ₹{remain:.0f}\n"

        if spent > budgets[cat]:
            report += f"  ⚠ Over budget in {cat}\n"

            if cat == "Food":
                report += "  Recommendation: Use hostel mess more often.\n"
            elif cat == "Snacks":
                report += "  Recommendation: Reduce daily snack purchases.\n"
            elif cat == "Travel":
                report += "  Recommendation: Combine trips home.\n"
            elif cat == "Outing":
                report += "  Recommendation: Skip outings this month.\n"

    report += "\n=====================\n"
    report += f"TOTAL BUDGET : ₹{total_budget}\n"
    report += f"TOTAL SPENT  : ₹{total_spent:.0f}\n"
    report += f"REMAINING    : ₹{total_budget-total_spent:.0f}\n"

    report_box.delete("1.0", tk.END)
    report_box.insert(tk.END, report)

def add_expense():
    try:
        amt = float(amount_var.get())
    except:
        messagebox.showerror("Error", "Enter valid amount")
        return

    expenses.append([
        date_var.get(),
        category_var.get(),
        desc_var.get(),
        amt
    ])

    refresh()

def set_budget():
    try:
        budgets[budget_cat.get()] = float(budget_amt.get())
        refresh()
        messagebox.showinfo("Success", "Budget Updated")
    except:
        messagebox.showerror("Error", "Invalid Budget")

root = tk.Tk()
root.title("Student Budget Companion")
root.geometry("1100x700")

title = tk.Label(root, text="PERSONAL BUDGET COMPANION", font=("Arial",18,"bold"))
title.pack(pady=10)

top = tk.Frame(root)
top.pack(fill="x")

# Budget Frame
budget_frame = tk.LabelFrame(top, text="Set Budget")
budget_frame.pack(side="left", padx=10, pady=10)

budget_cat = tk.StringVar(value="Food")
budget_amt = tk.StringVar()

ttk.Combobox(budget_frame, textvariable=budget_cat,
             values=list(budgets.keys()), width=20).grid(row=0,column=0,padx=5,pady=5)

tk.Entry(budget_frame, textvariable=budget_amt).grid(row=0,column=1,padx=5,pady=5)

tk.Button(budget_frame, text="Update Budget",
          command=set_budget).grid(row=0,column=2,padx=5,pady=5)

# Expense Frame
expense_frame = tk.LabelFrame(top, text="Add Expense")
expense_frame.pack(side="left", padx=10)

date_var = tk.StringVar(value=datetime.today().strftime("%Y-%m-%d"))
category_var = tk.StringVar(value="Food")
desc_var = tk.StringVar()
amount_var = tk.StringVar()

tk.Label(expense_frame,text="Date").grid(row=0,column=0)
tk.Entry(expense_frame,textvariable=date_var,width=12).grid(row=0,column=1)

tk.Label(expense_frame,text="Category").grid(row=1,column=0)

ttk.Combobox(expense_frame,textvariable=category_var,
             values=list(budgets.keys()),width=18).grid(row=1,column=1)

tk.Label(expense_frame,text="Description").grid(row=2,column=0)
tk.Entry(expense_frame,textvariable=desc_var).grid(row=2,column=1)

tk.Label(expense_frame,text="Amount").grid(row=3,column=0)
tk.Entry(expense_frame,textvariable=amount_var).grid(row=3,column=1)

tk.Button(expense_frame,text="Add Expense",
          command=add_expense).grid(row=4,column=0,columnspan=2,pady=5)

# Table
columns = ("Date","Category","Description","Amount")

tree = ttk.Treeview(root, columns=columns, show="headings", height=12)

for c in columns:
    tree.heading(c, text=c)
    tree.column(c, width=200)

tree.pack(fill="both", expand=True, padx=10, pady=10)

# Report
report_box = tk.Text(root, height=12)
report_box.pack(fill="both", padx=10, pady=10)

refresh()
root.mainloop()
