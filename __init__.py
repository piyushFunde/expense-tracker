import customtkinter as ctk
from tkinter import messagebox
import datetime
import json
import os
from tkinter import ttk

# Set appearance mode and color theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("💸 Expense Tracker Pro")
        self.root.geometry("1000x750")
        self.root.minsize(900, 650)
        
        # Theme variables
        self.dark_mode = False
        self.expenses = []
        self.total_expense = 0.0
        self.salary = 0.0
        self.data_file = "expenses_data.json"
        self.categories = ["Food", "Transport", "Entertainment", "Shopping", "Health", "Education", "Utilities", "Other"]
        
        # Color Schemes
        self.light_theme = {
            "bg": "#f5f5f5",
            "primary": "#3498db",
            "secondary": "#2ecc71",
            "danger": "#e74c3c",
            "warning": "#f39c12",
            "card": "#ffffff",
            "text": "#2c3e50",
            "light_text": "#7f8c8d"
        }
        
        self.dark_theme = {
            "bg": "#1e1e1e",
            "primary": "#3498db",
            "secondary": "#2ecc71",
            "danger": "#e74c3c",
            "warning": "#f39c12",
            "card": "#2d2d2d",
            "text": "#ecf0f1",
            "light_text": "#95a5a6"
        }
        
        self.current_theme = self.light_theme
        
        # Load expenses
        self.load_expenses()
        
        # Create UI
        self.create_ui()

    def create_ui(self):
        """Create the main user interface"""
        # Main container
        main_container = ctk.CTkFrame(self.root, fg_color=self.current_theme["bg"])
        main_container.pack(fill="both", expand=True)
        
        # Header
        self.create_header(main_container)
        
        # Content area with two columns
        content_frame = ctk.CTkFrame(main_container, fg_color=self.current_theme["bg"])
        content_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Left column
        left_column = ctk.CTkFrame(content_frame, fg_color=self.current_theme["bg"])
        left_column.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        # Right column
        right_column = ctk.CTkFrame(content_frame, fg_color=self.current_theme["bg"])
        right_column.pack(side="right", fill="both", expand=True, padx=(10, 0))
        
        # Add sections to left column
        self.create_expense_entry(left_column)
        self.create_salary_section(left_column)
        self.create_summary_panel(left_column)
        
        # Add sections to right column
        self.create_expense_log(right_column)
        
        # Status bar
        self.create_status_bar(main_container)
        
        # Refresh data
        self.refresh_expense_table()
        self.calculate_total()

    def create_header(self, parent):
        """Create modern header with theme toggle"""
        header = ctk.CTkFrame(parent, fg_color=self.current_theme["primary"], height=80)
        header.pack(fill="x", padx=0, pady=0)
        header.pack_propagate(False)
        
        # Left side - Title
        title_frame = ctk.CTkFrame(header, fg_color=self.current_theme["primary"])
        title_frame.pack(side="left", fill="both", expand=True, padx=20)
        
        title = ctk.CTkLabel(
            title_frame,
            text="💸 Expense Tracker Pro",
            font=("Helvetica", 28, "bold"),
            text_color="white"
        )
        title.pack(anchor="w", pady=10)
        
        subtitle = ctk.CTkLabel(
            title_frame,
            text="Manage your finances with ease",
            font=("Helvetica", 11),
            text_color="#ecf0f1"
        )
        subtitle.pack(anchor="w")
        
        # Right side - Theme toggle button
        toggle_btn = ctk.CTkButton(
            header,
            text="🌙 Dark Mode",
            font=("Helvetica", 10, "bold"),
            width=120,
            height=40,
            command=self.toggle_theme,
            fg_color="#2980b9",
            hover_color="#1f618d"
        )
        toggle_btn.pack(side="right", padx=20, pady=20)

    def create_expense_entry(self, parent):
        """Create expense entry card"""
        card = ctk.CTkFrame(parent, fg_color=self.current_theme["card"], corner_radius=10)
        card.pack(fill="x", pady=10)
        
        # Card header
        header = ctk.CTkLabel(
            card,
            text="📝 Add New Expense",
            font=("Helvetica", 14, "bold"),
            text_color=self.current_theme["primary"]
        )
        header.pack(anchor="w", padx=15, pady=(15, 10))
        
        # Amount
        ctk.CTkLabel(card, text="Amount (₹)", font=("Helvetica", 10, "bold"), text_color=self.current_theme["text"]).pack(anchor="w", padx=15, pady=(5, 0))
        self.expense_entry = ctk.CTkEntry(card, placeholder_text="Enter amount", height=35)
        self.expense_entry.pack(fill="x", padx=15, pady=(0, 10))
        
        # Category
        ctk.CTkLabel(card, text="Category", font=("Helvetica", 10, "bold"), text_color=self.current_theme["text"]).pack(anchor="w", padx=15, pady=(5, 0))
        self.category_combo = ctk.CTkComboBox(
            card,
            values=self.categories,
            height=35,
            state="readonly"
        )
        self.category_combo.pack(fill="x", padx=15, pady=(0, 10))
        self.category_combo.set(self.categories[0])
        
        # Comment
        ctk.CTkLabel(card, text="Comment (Optional)", font=("Helvetica", 10, "bold"), text_color=self.current_theme["text"]).pack(anchor="w", padx=15, pady=(5, 0))
        self.comment_entry = ctk.CTkEntry(card, placeholder_text="Add a note...", height=35)
        self.comment_entry.pack(fill="x", padx=15, pady=(0, 10))
        
        # Add button
        add_btn = ctk.CTkButton(
            card,
            text="➕ Add Expense",
            font=("Helvetica", 12, "bold"),
            height=40,
            command=self.add_expense,
            fg_color=self.current_theme["secondary"],
            hover_color="#27ae60"
        )
        add_btn.pack(fill="x", padx=15, pady=15)

    def create_salary_section(self, parent):
        """Create salary entry card"""
        card = ctk.CTkFrame(parent, fg_color=self.current_theme["card"], corner_radius=10)
        card.pack(fill="x", pady=10)
        
        header = ctk.CTkLabel(
            card,
            text="💰 Salary Information",
            font=("Helvetica", 14, "bold"),
            text_color=self.current_theme["primary"]
        )
        header.pack(anchor="w", padx=15, pady=(15, 10))
        
        ctk.CTkLabel(card, text="Monthly Salary (₹)", font=("Helvetica", 10, "bold"), text_color=self.current_theme["text"]).pack(anchor="w", padx=15, pady=(5, 0))
        self.salary_entry = ctk.CTkEntry(card, placeholder_text="Enter salary", height=35)
        self.salary_entry.pack(fill="x", padx=15, pady=(0, 10))
        
        calc_btn = ctk.CTkButton(
            card,
            text="📊 Calculate Total",
            font=("Helvetica", 12, "bold"),
            height=40,
            command=self.calculate_total,
            fg_color=self.current_theme["primary"],
            hover_color="#2980b9"
        )
        calc_btn.pack(fill="x", padx=15, pady=15)

    def create_summary_panel(self, parent):
        """Create summary statistics panel"""
        card = ctk.CTkFrame(parent, fg_color=self.current_theme["card"], corner_radius=10)
        card.pack(fill="x", pady=10)
        
        header = ctk.CTkLabel(
            card,
            text="📈 Financial Summary",
            font=("Helvetica", 14, "bold"),
            text_color=self.current_theme["primary"]
        )
        header.pack(anchor="w", padx=15, pady=(15, 10))
        
        # Summary items
        summary_frame = ctk.CTkFrame(card, fg_color=self.current_theme["card"])
        summary_frame.pack(fill="x", padx=15, pady=10)
        
        # Total expenses
        self.total_label = ctk.CTkLabel(
            summary_frame,
            text="💷 Total Expenses: ₹0.00",
            font=("Helvetica", 11, "bold"),
            text_color=self.current_theme["text"]
        )
        self.total_label.pack(anchor="w", pady=5)
        
        # Remaining
        self.remaining_label = ctk.CTkLabel(
            summary_frame,
            text="💰 Remaining: ₹0.00",
            font=("Helvetica", 11, "bold"),
            text_color=self.current_theme["text"]
        )
        self.remaining_label.pack(anchor="w", pady=5)
        
        # Percentage
        self.percentage_label = ctk.CTkLabel(
            summary_frame,
            text="📊 Spent: 0%",
            font=("Helvetica", 11, "bold"),
            text_color=self.current_theme["text"]
        )
        self.percentage_label.pack(anchor="w", pady=5)
        
        # Status
        self.status_label = ctk.CTkLabel(
            summary_frame,
            text="🟢 Healthy Budget",
            font=("Helvetica", 11, "bold"),
            text_color=self.current_theme["secondary"]
        )
        self.status_label.pack(anchor="w", pady=5)
        
        # Highest category
        self.top_category_label = ctk.CTkLabel(
            summary_frame,
            text="🏆 Top Category: N/A",
            font=("Helvetica", 11, "bold"),
            text_color=self.current_theme["text"]
        )
        self.top_category_label.pack(anchor="w", pady=5)

    def create_expense_log(self, parent):
        """Create modern expense log with Treeview"""
        card = ctk.CTkFrame(parent, fg_color=self.current_theme["card"], corner_radius=10)
        card.pack(fill="both", expand=True, pady=10)
        
        header = ctk.CTkLabel(
            card,
            text="📋 Expense History",
            font=("Helvetica", 14, "bold"),
            text_color=self.current_theme["primary"]
        )
        header.pack(anchor="w", padx=15, pady=(15, 10))
        
        # Treeview frame
        tree_frame = ctk.CTkFrame(card, fg_color=self.current_theme["card"])
        tree_frame.pack(fill="both", expand=True, padx=15, pady=10)
        
        # Create Treeview
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', font=('Helvetica', 10), rowheight=25)
        style.configure('Treeview.Heading', font=('Helvetica', 11, 'bold'))
        
        self.tree = ttk.Treeview(
            tree_frame,
            columns=("Amount", "Category", "Comment", "Date"),
            show="headings",
            height=15
        )
        
        # Define columns
        self.tree.column("Amount", width=80, anchor="center")
        self.tree.column("Category", width=100, anchor="center")
        self.tree.column("Comment", width=150, anchor="w")
        self.tree.column("Date", width=120, anchor="center")
        
        # Define headings
        self.tree.heading("Amount", text="Amount (₹)")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Comment", text="Comment")
        self.tree.heading("Date", text="Date & Time")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Delete button
        delete_btn = ctk.CTkButton(
            card,
            text="🗑️ Delete Selected",
            font=("Helvetica", 11, "bold"),
            height=35,
            command=self.delete_expense,
            fg_color=self.current_theme["danger"],
            hover_color="#c0392b"
        )
        delete_btn.pack(fill="x", padx=15, pady=15)

    def create_status_bar(self, parent):
        """Create status bar at bottom"""
        status_frame = ctk.CTkFrame(parent, fg_color=self.current_theme["primary"], height=40)
        status_frame.pack(fill="x", padx=0, pady=0)
        status_frame.pack_propagate(False)
        
        self.status_message = ctk.CTkLabel(
            status_frame,
            text="✅ Ready",
            font=("Helvetica", 10),
            text_color="white"
        )
        self.status_message.pack(anchor="w", padx=20, pady=10)

    def update_status(self, message, duration=3000):
        """Update status bar message"""
        self.status_message.configure(text=message)
        self.root.after(duration, lambda: self.status_message.configure(text="✅ Ready"))

    def toggle_theme(self):
        """Toggle between dark and light mode"""
        self.dark_mode = not self.dark_mode
        
        if self.dark_mode:
            ctk.set_appearance_mode("dark")
            self.current_theme = self.dark_theme
            self.status_message.configure(text="🌙 Dark Mode Enabled")
        else:
            ctk.set_appearance_mode("light")
            self.current_theme = self.light_theme
            self.status_message.configure(text="☀️ Light Mode Enabled")
        
        # Recreate UI
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_ui()
        self.root.after(2000, lambda: self.update_status("✅ Ready"))

    def load_expenses(self):
        """Load expenses from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    self.expenses = json.load(file)
            else:
                self.expenses = []
        except json.JSONDecodeError:
            messagebox.showerror("❌ Error", "Corrupted data file. Starting fresh.")
            self.expenses = []

    def save_expenses(self):
        """Save expenses to JSON file"""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.expenses, file, indent=2)
        except IOError:
            messagebox.showerror("❌ Error", "Failed to save expenses.")
            self.update_status("❌ Failed to save")

    def refresh_expense_table(self):
        """Refresh the Treeview table"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Insert expenses
        for expense in self.expenses:
            self.tree.insert(
                "",
                "end",
                values=(
                    f"₹{expense['expense']:.2f}",
                    expense['category'],
                    expense['comment'],
                    expense['date']
                )
            )

    def add_expense(self):
        """Add a new expense"""
        expense = self.expense_entry.get().strip()
        category = self.category_combo.get()
        comment = self.comment_entry.get().strip()
        
        if not expense:
            messagebox.showerror("⚠️ Validation Error", "Please enter an amount.")
            self.update_status("❌ Enter amount")
            return
        
        try:
            expense = float(expense)
            if expense <= 0:
                messagebox.showerror("⚠️ Validation Error", "Amount must be greater than 0.")
                self.update_status("❌ Invalid amount")
                return
        except ValueError:
            messagebox.showerror("⚠️ Validation Error", "Please enter a valid number.")
            self.update_status("❌ Invalid input")
            return
        
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        expense_data = {
            "expense": expense,
            "category": category,
            "comment": comment if comment else "N/A",
            "date": current_time
        }
        
        self.expenses.append(expense_data)
        self.save_expenses()
        self.refresh_expense_table()
        self.calculate_total()
        
        # Clear inputs
        self.expense_entry.delete(0, "end")
        self.comment_entry.delete(0, "end")
        self.category_combo.set(self.categories[0])
        
        self.update_status(f"✅ Added ₹{expense:.2f} to {category}")

    def calculate_total(self):
        """Calculate total expenses and update summary"""
        if self.expenses:
            self.total_expense = sum(item['expense'] for item in self.expenses)
        else:
            self.total_expense = 0.0
        
        salary_str = self.salary_entry.get().strip()
        
        if not salary_str:
            self.total_label.configure(text=f"💷 Total Expenses: ₹{self.total_expense:.2f}")
            self.remaining_label.configure(text="💰 Remaining: Enter salary")
            self.percentage_label.configure(text="📊 Spent: 0%")
            self.status_label.configure(text="ℹ️ Enter salary")
            self.update_status("ℹ️ Enter salary for analysis")
            return
        
        try:
            self.salary = float(salary_str)
            if self.salary <= 0:
                messagebox.showerror("⚠️ Validation Error", "Salary must be greater than 0.")
                self.salary_entry.delete(0, "end")
                return
        except ValueError:
            messagebox.showerror("⚠️ Validation Error", "Please enter a valid salary.")
            return
        
        remaining = self.salary - self.total_expense
        percentage = (self.total_expense / self.salary) * 100 if self.salary > 0 else 0
        
        # Update labels
        self.total_label.configure(text=f"💷 Total Expenses: ₹{self.total_expense:.2f}")
        self.remaining_label.configure(text=f"💰 Remaining: ₹{remaining:.2f}")
        self.percentage_label.configure(text=f"📊 Spent: {percentage:.1f}%")
        
        # Status color
        if remaining < 0:
            status = "🔴 OVER BUDGET"
            color = self.current_theme["danger"]
        elif remaining < self.salary * 0.20:
            status = "🟠 LOW BUDGET"
            color = self.current_theme["warning"]
        else:
            status = "🟢 HEALTHY"
            color = self.current_theme["secondary"]
        
        self.status_label.configure(text=status, text_color=color)
        
        # Top category
        if self.expenses:
            category_sum = {}
            for expense in self.expenses:
                cat = expense['category']
                category_sum[cat] = category_sum.get(cat, 0) + expense['expense']
            
            top_cat = max(category_sum, key=category_sum.get)
            self.top_category_label.configure(
                text=f"🏆 Top Category: {top_cat} (₹{category_sum[top_cat]:.2f})"
            )
        else:
            self.top_category_label.configure(text="🏆 Top Category: N/A")

    def delete_expense(self):
        """Delete selected expense"""
        selection = self.tree.selection()
        
        if not selection:
            messagebox.showwarning("⚠️ No Selection", "Please select an expense to delete.")
            self.update_status("❌ Select expense to delete")
            return
        
        response = messagebox.askyesno("🗑️ Confirm", "Are you sure you want to delete this expense?")
        
        if not response:
            return
        
        # Get indices and delete in reverse order
        indices = [self.tree.index(item) for item in selection]
        for idx in sorted(indices, reverse=True):
            del self.expenses[idx]
        
        self.save_expenses()
        self.refresh_expense_table()
        self.calculate_total()
        self.update_status("✅ Expense deleted successfully")


def main():
    """Main function"""
    root = ctk.CTk()
    app = ExpenseTracker(root)
    root.mainloop()


if __name__ == "__main__":
    main()