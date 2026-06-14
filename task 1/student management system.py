from tkinter import *
from tkinter import ttk, messagebox

students = []

# ---------------- FUNCTIONS ----------------

def add_student():
    if id_var.get() == "" or name_var.get() == "":
        messagebox.showerror("Error", "ID and Name are required")
        return

    students.append([
        id_var.get(),
        name_var.get(),
        dept_var.get(),
        marks_var.get(),
        attendance_var.get()
    ])

    refresh_table()
    clear_fields()

def refresh_table():
    tree.delete(*tree.get_children())

    for student in students:
        tree.insert("", END, values=student)

def clear_fields():
    id_var.set("")
    name_var.set("")
    dept_var.set("")
    marks_var.set("")
    attendance_var.set("")

def select_student(event):
    selected = tree.focus()

    if not selected:
        return

    values = tree.item(selected, "values")

    id_var.set(values[0])
    name_var.set(values[1])
    dept_var.set(values[2])
    marks_var.set(values[3])
    attendance_var.set(values[4])

def update_student():
    selected = tree.focus()

    if not selected:
        messagebox.showwarning("Warning", "Select a student")
        return

    tree.item(selected, values=(
        id_var.get(),
        name_var.get(),
        dept_var.get(),
        marks_var.get(),
        attendance_var.get()
    ))

    index = tree.index(selected)

    students[index] = [
        id_var.get(),
        name_var.get(),
        dept_var.get(),
        marks_var.get(),
        attendance_var.get()
    ]

    clear_fields()

def delete_student():
    selected = tree.focus()

    if not selected:
        messagebox.showwarning("Warning", "Select a student")
        return

    index = tree.index(selected)

    del students[index]
    tree.delete(selected)

def search_student():
    keyword = search_var.get().lower()

    tree.delete(*tree.get_children())

    for student in students:
        if keyword in student[1].lower():
            tree.insert("", END, values=student)

# ---------------- GUI ----------------

root = Tk()
root.title("Student Management System")
root.geometry("900x550")
root.configure(bg="lightblue")

title = Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold"),
    bg="navy",
    fg="white"
)
title.pack(fill=X)

# -------- FORM --------

frame = Frame(root, bg="lightblue")
frame.pack(pady=10)

id_var = StringVar()
name_var = StringVar()
dept_var = StringVar()
marks_var = StringVar()
attendance_var = StringVar()
search_var = StringVar()

Label(frame, text="Student ID").grid(row=0, column=0, padx=10, pady=5)
Entry(frame, textvariable=id_var).grid(row=0, column=1)

Label(frame, text="Name").grid(row=1, column=0, padx=10, pady=5)
Entry(frame, textvariable=name_var).grid(row=1, column=1)

Label(frame, text="Department").grid(row=2, column=0, padx=10, pady=5)
Entry(frame, textvariable=dept_var).grid(row=2, column=1)

Label(frame, text="Marks").grid(row=3, column=0, padx=10, pady=5)
Entry(frame, textvariable=marks_var).grid(row=3, column=1)

Label(frame, text="Attendance").grid(row=4, column=0, padx=10, pady=5)
Entry(frame, textvariable=attendance_var).grid(row=4, column=1)

# -------- BUTTONS --------

btn_frame = Frame(root, bg="lightblue")
btn_frame.pack()

Button(btn_frame, text="Add", width=12,
       command=add_student).grid(row=0, column=0, padx=5)

Button(btn_frame, text="Update", width=12,
       command=update_student).grid(row=0, column=1, padx=5)

Button(btn_frame, text="Delete", width=12,
       command=delete_student).grid(row=0, column=2, padx=5)

Button(btn_frame, text="Clear", width=12,
       command=clear_fields).grid(row=0, column=3, padx=5)

# -------- SEARCH --------

search_frame = Frame(root, bg="lightblue")
search_frame.pack(pady=10)

Entry(search_frame,
      textvariable=search_var,
      width=30).grid(row=0, column=0)

Button(search_frame,
       text="Search",
       command=search_student).grid(row=0, column=1, padx=5)

# -------- TABLE --------

table_frame = Frame(root)
table_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

columns = (
    "ID",
    "Name",
    "Department",
    "Marks",
    "Attendance"
)

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill=BOTH, expand=True)

tree.bind("<ButtonRelease-1>", select_student)

# -------- SAMPLE DATA --------

students.extend([
    ["101", "Arun", "CSE", "85", "Present"],
    ["102", "Priya", "AIML", "90", "Present"],
    ["103", "Rahul", "ECE", "78", "Absent"]
])

refresh_table()

root.mainloop()
