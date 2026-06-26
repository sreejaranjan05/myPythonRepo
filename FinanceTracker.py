import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
import matplotlib.pyplot as plt
DATA_FILES = "Finance_Data.csv"
if not os.path.exists(DATA_FILES):
    with open(DATA_FILES, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Amount", "Category", "Type"])
def add_transaction():
    amount = amount_entry.get()
    category = category_entry.get()
    t_type = type_combobox.get()
    if not amount or not category or not t_type:
        messagebox.showerror("Error", "Please fill out all fields")
        return
    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a valid number")
        return
    with open(DATA_FILES, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([amount, category, t_type])
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

    messagebox.showinfo("success","Transaction recorded successfully")
    update_summary()

def update_summary():
    total_income=0.0
    total_expense = 0.0

    for row in tree.get_children():
        tree.delete(row)
    if os.path.exists(DATA_FILES):
        with open(DATA_FILES,"r") as f:
            reader=csv.reader(f)
            next(reader)
            for row in reader:
                if not row: continue
                tree.insert('', tk.END, values=row)
                amt=float(row[0])
                if row[2] == "Income":
                    total_income += amt
                else:
                    total_expense += amt
    balance = total_income - total_expense
    balance_label.config(text=f"Current balance: ₹{balance:.2f}" , fg="#abf7db" if balance >= 0 else "#fa9699")

def show_graph():
    category_expenses = {}

    if os.path.exists(DATA_FILES):
        with open(DATA_FILES, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if not row: continue
                amount = float(row[0])
                category = row[1]
                t_type = row[2]

                if t_type == "Expense":
                    if category in category_expenses:
                        category_expenses[category] += amount
                    else:
                        category_expenses[category] = amount
    if not category_expenses:
        messagebox.showerror("Error", "No expenses to plot graph")
        return

    categories = list(category_expenses.keys())
    amounts = list(category_expenses.values())

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Expense Breakdown by Category")
    plt.show()

root=tk.Tk()
root.title("UrVaultWallet - Personal Finance Tracker")
root.geometry("600x600")
root.config(bg="#f5f5f2")

#black and pink
title = tk.Label(root, text="✮⋆˙Ur Vault Wallet˙⋆✮", font=("Times New Roman", 28, "bold"), bg="#faf18e", fg="#fa0598")
title.pack(padx=10, pady=20)

#light pink
input_frame=tk.LabelFrame(root, text="", bg="#f5c1f1", bd=4, relief="raised", padx=10, pady=10)
input_frame.pack(padx=30, fill='x', pady=10)

#yellow and blue
frame_title = tk.Label(
    input_frame,
    text=" Add new Transaction ",
    font=("fixedsys", 16, "bold"),
    bg="#faf18e",
    bd=4,
    relief='raised',
    fg="#4681e0"
)
frame_title.grid(row=0, column=0, columnspan=2, pady=(0, 15))

#light pink and dark pink
tk.Label(input_frame,
         text='Amount (₹)',
         font=('fixedsys', 12),
         bg='#b8def5',
         bd=6,
         relief="raised",
         fg="#b80789"
         ).grid(row=1, column=0, sticky="w", pady=4)

#mid-pink and black
amount_entry = tk.Entry(input_frame, bg="#fc79dc", bd=4, relief="sunken", fg="#00011a", insertbackground="#00011a")
amount_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

#light pink and dark pink
tk.Label(input_frame,
         text="Category:",
         font=('fixedsys', 12),
         bg='#b8def5',
         bd=6,
         relief="raised",
         fg="#b80789"
         ).grid(row=2, column=0, sticky="w", pady=4)
#mid-pink, black
category_entry = tk.Entry(input_frame, bg="#fc79dc", bd=4, relief="sunken", fg="#00011a", insertbackground="#00011a")
category_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")

#light pink and dark pink
tk.Label(input_frame,
         text="Type:",
         font=('fixedsys', 12),
         bg="#b8def5",
         bd=6,
         relief="raised",
         fg="#b80789"
         ).grid(row=3, column=0, sticky="w", pady=4)

type_combobox = ttk.Combobox(input_frame,
                             values=["Income", "Expense"],
                             state="readonly",)
type_combobox.grid(row=3, column=1, pady=4, padx=5, sticky="ew")

#coral and yellow
add_btn = tk.Button(input_frame,
                    text="Add Transaction",
                    font=('fixedsys', 14),
                    command=add_transaction,
                    bg="#ff78a5",
                    bd=9,
                    relief="sunken",
                    fg="#faf18e",
                    )
add_btn.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

#dark pink and light pink
balance_label = tk.Label(root,
                         text="Current Balance: ₹0.00",
                         font=('fixedsys', 16),
                         bg="#00011a",
                        )
balance_label.pack(pady=10)

#yellow and blue
graph_btn = tk.Button(root,
                      text="📊 Show Expense Graph",
                      command=show_graph,
                      bg="#faf18e",
                      fg="#4681e0",
                      font=('fixedsys', 16)
                      )
graph_btn.pack(pady=5)

tree_frame = tk.Frame(root, bg="#ccfce5")
tree_frame.pack(pady=10, fill="both", expand=True, padx=20)

columns = ("Amount", "Category", "Type")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=6)
tree.heading("Amount", text="Amount (₹)")
tree.heading("Category", text="Category")
tree.heading("Type", text="Type")

tree.column("Amount", width=100, anchor="center")
tree.column("Category", width=200, anchor="w")
tree.column("Type", width=100, anchor="center")
tree.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

update_summary()
root.mainloop()


