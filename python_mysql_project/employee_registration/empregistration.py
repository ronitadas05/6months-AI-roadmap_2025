import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ------------------- DATABASE CONNECTION -------------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",               # MySQL username
        password="123456",  # MySQL password
        database="webgui"
    )

# ------------------- SUBMIT FUNCTION -------------------
def submit_data():
    empid = entry_id.get()
    name = entry_name.get()
    mobile = entry_mobile.get()
    salary = entry_salary.get()

    if not (empid and name and mobile and salary):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        con = connect_db()
        cursor = con.cursor()
        query = "INSERT INTO employees (emp_id, name, mobile, salary) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (empid, name, mobile, float(salary)))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Employee registered successfully.")
        clear_fields()
        fetch_data()  # refresh table
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# ------------------- CLEAR FUNCTION -------------------
def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    entry_salary.delete(0, tk.END)


def update_employee():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Select Record", "Please select a row to update.")
        return

    values = tree.item(selected, "values")
    old_emp_id = values[0]  # The original emp_id in DB

    # New values from entry fields
    new_emp_id = entry_id.get()
    name = entry_name.get()
    mobile = entry_mobile.get()
    salary = entry_salary.get()

    if not (new_emp_id and name and mobile and salary):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        con = connect_db()
        cursor = con.cursor()
        query = """
            UPDATE employees 
            SET emp_id = %s, name = %s, mobile = %s, salary = %s 
            WHERE emp_id = %s
        """
        cursor.execute(query, (new_emp_id, name, mobile, float(salary), old_emp_id))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Employee record updated successfully.")
        fetch_data()
        clear_fields()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))


def delete_employee():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Select Record", "Please select a row to delete.")
        return

    values = tree.item(selected, "values")
    emp_id = values[0]  # Get emp_id from selected row

    confirm = messagebox.askyesno("Confirm Delete", f"Delete employee ID {emp_id}?")
    if not confirm:
        return

    try:
        con = connect_db()
        cursor = con.cursor()
        cursor.execute("DELETE FROM employees WHERE emp_id = %s", (emp_id,))
        con.commit()
        con.close()

        tree.delete(selected)  # Remove from Treeview
        messagebox.showinfo("Deleted", f"Employee {emp_id} deleted successfully.")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))


# ------------------- FETCH & DISPLAY DATA -------------------
def fetch_data():
    for row in tree.get_children():
        tree.delete(row)

    try:
        con = connect_db()
        cursor = con.cursor()
        cursor.execute("SELECT emp_id, name, mobile, salary FROM employees")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        con.close()
    except Exception as e:
        messagebox.showerror("Fetch Error", str(e))

# ------------------- GUI SETUP -------------------
root = tk.Tk()
root.geometry("800x600")
root.title("Employee Registration System")

# --- Input Form ---
tk.Label(root, text="Employee Registration", font=("Arial", 18), fg="blue").pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Employee ID").grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(form_frame)
entry_id.grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Name").grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(form_frame)
entry_name.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Mobile").grid(row=2, column=0, padx=10, pady=5)
entry_mobile = tk.Entry(form_frame)
entry_mobile.grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Salary").grid(row=3, column=0, padx=10, pady=5)
entry_salary = tk.Entry(form_frame)
entry_salary.grid(row=3, column=1, pady=5)

def load_selected_row():
    selected = tree.focus()
    if not selected:
        return

    values = tree.item(selected, "values")
    entry_id.delete(0, tk.END)
    entry_id.insert(0, values[0])
    
    entry_name.delete(0, tk.END)
    entry_name.insert(0, values[1])
    
    entry_mobile.delete(0, tk.END)
    entry_mobile.insert(0, values[2])
    
    entry_salary.delete(0, tk.END)
    entry_salary.insert(0, values[3])

tk.Button(form_frame, text="Submit", command=submit_data, bg="green", fg="white", width=15).grid(row=4, columnspan=2, pady=10)

tk.Button(form_frame, text="Delete Selected", command=delete_employee, bg="red", fg="white", width=15).grid(row=5, columnspan=2, pady=5)

tk.Button(form_frame, text="Update Selected", command=update_employee, bg="orange", fg="white", width=15).grid(row=6, columnspan=2, pady=5)

tk.Button(form_frame, text="Clear", command=clear_fields, bg="gray", fg="white", width=15).grid(row=7, columnspan=2, pady=5)




# --- Table View ---
table_frame = tk.Frame(root)
table_frame.pack(pady=10, fill=tk.BOTH, expand=True)

columns = ("emp_id", "name", "mobile", "salary")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col.capitalize())
    tree.column(col, width=150)

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill="y")

tree.bind("<<TreeviewSelect>>", lambda e: load_selected_row())

# Fetch data on launch
fetch_data()

root.mainloop()
