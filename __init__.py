import tkinter as tk
from tkinter import messagebox
import datetime


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("💸 Expense Tracker")
        self.root.geometry("500x600")
        self.root.configure(bg="#f7f7f7")

        self.expenses = []
        self.total_expense = 0
        self.salary = 0

        title_label = tk.Label(root, text="Expense Tracker", font=("Helvetica", 18, "bold"), fg="#333", bg="#f7f7f7")
        title_label.pack(pady=10)

        # Expense Entry
        expense_frame = tk.LabelFrame(root, text="Add Expense", padx=10, pady=10, bg="#ffffff",
                                      font=("Helvetica", 10, "bold"))
        expense_frame.pack(padx=20, pady=10, fill="x")

        tk.Label(expense_frame, text="Amount (₹):", bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
        self.expense_entry = tk.Entry(expense_frame, width=25)
        self.expense_entry.grid(row=0, column=1, pady=5)

        tk.Label(expense_frame, text="Category:", bg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
        self.expense_category_entry = tk.Entry(expense_frame, width=25)
        self.expense_category_entry.grid(row=1, column=1, pady=5)

        tk.Label(expense_frame, text="Comments:", bg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)
        self.comment_entry = tk.Entry(expense_frame, width=25)
        self.comment_entry.grid(row=2, column=1, pady=5)

        self.add_button = tk.Button(expense_frame, text="➕ Add Expense", command=self.add_expense, bg="#4CAF50",
                                    fg="white", font=("Helvetica", 10, "bold"))
        self.add_button.grid(row=3, columnspan=2, pady=10)

        # Salary Entry
        salary_frame = tk.LabelFrame(root, text="Salary Info", padx=10, pady=10, bg="#ffffff",
                                     font=("Helvetica", 10, "bold"))
        salary_frame.pack(padx=20, pady=10, fill="x")

        tk.Label(salary_frame, text="Your Salary (₹):", bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
        self.salary_entry = tk.Entry(salary_frame, width=25)
        self.salary_entry.grid(row=0, column=1, pady=5)

        self.calculate_button = tk.Button(salary_frame, text="📊 Calculate Total", command=self.calculate_total,
                                          bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"))
        self.calculate_button.grid(row=1, columnspan=2, pady=10)

        # Total Display
        self.total_label = tk.Label(root, text="Total Expenses: ₹0", font=("Helvetica", 12, "bold"), fg="#333",
                                    bg="#f7f7f7")
        self.total_label.pack(pady=10)

        # Listbox with Scrollbar
        listbox_frame = tk.LabelFrame(root, text="Expense Log", padx=5, pady=5, bg="#ffffff",
                                      font=("Helvetica", 10, "bold"))
        listbox_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.expense_listbox = tk.Listbox(listbox_frame, width=60, height=10)
        self.expense_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")
        scrollbar.config(command=self.expense_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.expense_listbox.config(yscrollcommand=scrollbar.set)

        # Add a Delete button for expenses
        self.delete_button = tk.Button(listbox_frame, text="🗑️ Delete Selected", command=self.delete_expense,
                                       bg="#F44336", fg="white", font=("Helvetica", 10, "bold"))
        self.delete_button.pack(pady=5)  # Placed inside listbox_frame for better grouping

    def add_expense(self):
        expense = self.expense_entry.get()
        category = self.expense_category_entry.get()
        comment = self.comment_entry.get()

        if not expense or not category:
            messagebox.showerror("Error", "Please enter both expense and category.")
            return

        try:
            expense = float(expense)
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number for expense.")
            return

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        expense_data = {"expense": expense, "category": category, "comment": comment, "date": current_time}
        self.expenses.append(expense_data)

        formatted = f"₹{expense:.2f} ({category}) : {comment} [{current_time}]"
        self.expense_listbox.insert(tk.END, formatted)

        self.expense_entry.delete(0, 'end')
        self.expense_category_entry.delete(0, 'end')
        self.comment_entry.delete(0, 'end')

        self.calculate_total()  # Automatically update total after adding an expense

    def calculate_total(self):
        salary = self.salary_entry.get()
        if not salary:
            # Only show error if salary is explicitly being calculated, not on expense add
            if self.expenses:  # If expenses exist, still show total expenses
                self.total_expense = sum(item['expense'] for item in self.expenses)
                self.total_label.config(text=f"Total Expenses: ₹{self.total_expense:.2f}")
            else:
                self.total_label.config(text="Total Expenses: ₹0")
            return

        try:
            self.salary = float(salary)
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number for salary.")
            return

        self.total_expense = sum(item['expense'] for item in self.expenses)
        remaining = self.salary - self.total_expense

        # Dynamic coloring for remaining balance
        if remaining < 0:
            remaining_color = "red"
        elif remaining < self.salary * 0.20:  # Less than 20% of salary remaining
            remaining_color = "orange"
        else:
            remaining_color = "green"

        self.total_label.config(text=f"Total Expenses: ₹{self.total_expense:.2f} | Remaining: ₹{remaining:.2f}",
                                fg=remaining_color)

    def delete_expense(self):
        selected_indices = self.expense_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("No Selection", "Please select an expense to delete.")
            return

        for index in selected_indices[::-1]:  # Delete from end to avoid index issues
            self.expense_listbox.delete(index)
            del self.expenses[index]

        self.calculate_total()  # Recalculate total after deletion


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()