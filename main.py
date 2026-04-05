import customtkinter as ctk
from tkinter import messagebox, ttk
import datetime
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Local imports
from database import DatabaseManager
from styles import LIGHT_THEME, DARK_THEME, CATEGORIES, FONT_H1, FONT_H2, FONT_BODY, FONT_BODY_BOLD, FONT_SMALL_BOLD
from app_logic import calculate_financials, generate_category_chart

# Set appearance mode and color theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💸 Expense Tracker Pro")
        self.root.geometry("1100x800")
        self.root.minsize(1000, 700)
        
        # Core Managers
        self.db = DatabaseManager()
        
        # State Variables
        self.dark_mode = False
        self.current_theme = LIGHT_THEME
        self.expenses = []
        self.salary = 0.0
        self.chart_canvas = None
        self.search_var = ctk.StringVar()
        self.search_var.trace_add("write", lambda *args: self.refresh_ui_data())
        
        # Setup migrations feedback if any
        migration_status, message = self.db.setup_database()
        if migration_status is True:
            messagebox.showinfo("✅ Success", message)
        elif migration_status is False:
            messagebox.showerror("❌ Migration Error", message)

        self.load_data()
        self.create_ui()

    def load_data(self):
        """Load data from database into memory"""
        try:
            self.expenses = self.db.load_expenses()
        except Exception as e:
            messagebox.showerror("❌ Error", str(e))
            self.expenses = []

    def create_ui(self):
        """Create the main user interface"""
        # Main container
        self.main_container = ctk.CTkFrame(self.root, fg_color=self.current_theme["bg"])
        self.main_container.pack(fill="both", expand=True)
        
        # Header
        self.create_header(self.main_container)
        
        # Content area with scrollable content or grid
        content_frame = ctk.CTkFrame(self.main_container, fg_color=self.current_theme["bg"])
        content_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Left column (Entry & Summary)
        left_column = ctk.CTkFrame(content_frame, fg_color=self.current_theme["bg"], width=350)
        left_column.pack(side="left", fill="both", expand=False, padx=(0, 10))
        left_column.pack_propagate(False)
        
        # Right column (History & Analysis)
        right_column = ctk.CTkFrame(content_frame, fg_color=self.current_theme["bg"])
        right_column.pack(side="left", fill="both", expand=True, padx=(10, 0))
        
        # Add sections to left column
        self.create_expense_entry(left_column)
        self.create_salary_section(left_column)
        self.create_summary_panel(left_column)
        
        # Add sections to right column
        right_tabs = ctk.CTkTabview(right_column, fg_color=self.current_theme["card"], segmented_button_selected_color=self.current_theme["primary"])
        right_tabs.pack(fill="both", expand=True)
        
        self.tab_history = right_tabs.add("📋 History")
        self.tab_analysis = right_tabs.add("📊 Analysis")
        
        self.create_expense_log(self.tab_history)
        self.create_analysis_tab(self.tab_analysis)
        
        # Status bar
        self.create_status_bar(self.main_container)
        
        # Refresh calculations and table
        self.refresh_ui_data()

    def create_header(self, parent):
        """Create modern header with theme toggle"""
        header = ctk.CTkFrame(parent, fg_color=self.current_theme["primary"], height=80)
        header.pack(fill="x", padx=0, pady=0)
        header.pack_propagate(False)
        
        # Title
        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack(side="left", fill="y", padx=20)
        
        ctk.CTkLabel(title_frame, text="💸 Expense Tracker Pro", font=FONT_H1, text_color="white").pack(anchor="w", pady=(10, 0))
        ctk.CTkLabel(title_frame, text="Manage your finances with ease", font=FONT_BODY, text_color="#ecf0f1").pack(anchor="w")
        
        # Theme toggle
        btn_text = "☀️ Light Mode" if self.dark_mode else "🌙 Dark Mode"
        toggle_btn = ctk.CTkButton(
            header,
            text=btn_text,
            font=FONT_SMALL_BOLD,
            width=120,
            height=40,
            command=self.toggle_theme,
            fg_color="#2980b9",
            hover_color="#1f618d"
        )
        toggle_btn.pack(side="right", padx=20)

    def create_expense_entry(self, parent):
        """Create expense entry card"""
        card = ctk.CTkFrame(parent, fg_color=self.current_theme["card"], corner_radius=10)
        card.pack(fill="x", pady=(0, 10))
        
        ctk.CTkLabel(card, text="📝 Add New Expense", font=FONT_H2, text_color=self.current_theme["primary"]).pack(anchor="w", padx=15, pady=(15, 10))
        
        # Amount
        ctk.CTkLabel(card, text="Amount (₹)", font=FONT_SMALL_BOLD, text_color=self.current_theme["text"]).pack(anchor="w", padx=15)
        self.expense_entry = ctk.CTkEntry(card, placeholder_text="Enter amount", height=35)
        self.expense_entry.pack(fill="x", padx=15, pady=(0, 10))
        
        # Category
        ctk.CTkLabel(card, text="Category", font=FONT_SMALL_BOLD, text_color=self.current_theme["text"]).pack(anchor="w", padx=15)
        self.category_combo = ctk.CTkComboBox(card, values=CATEGORIES, height=35, state="readonly")
        self.category_combo.pack(fill="x", padx=15, pady=(0, 10))
        self.category_combo.set(CATEGORIES[0])
        
        # Comment
        ctk.CTkLabel(card, text="Comment (Optional)", font=FONT_SMALL_BOLD, text_color=self.current_theme["text"]).pack(anchor="w", padx=15)
        self.comment_entry = ctk.CTkEntry(card, placeholder_text="Add a note...", height=35)
        self.comment_entry.pack(fill="x", padx=15, pady=(0, 10))
        
        # Add button
        ctk.CTkButton(
            card,
            text="➕ Add Expense",
            font=FONT_BODY_BOLD,
            height=40,
            command=self.add_expense,
            fg_color=self.current_theme["secondary"],
            hover_color="#27ae60"
        ).pack(fill="x", padx=15, pady=15)

    def create_salary_section(self, parent):
        """Create salary entry card"""
        card = ctk.CTkFrame(parent, fg_color=self.current_theme["card"], corner_radius=10)
        card.pack(fill="x", pady=10)
        
        ctk.CTkLabel(card, text="💰 Salary Information", font=FONT_H2, text_color=self.current_theme["primary"]).pack(anchor="w", padx=15, pady=(15, 10))
        
        self.salary_entry = ctk.CTkEntry(card, placeholder_text="Enter monthly salary", height=35)
        self.salary_entry.pack(fill="x", padx=15, pady=(0, 10))
        
        ctk.CTkButton(
            card,
            text="📊 Update Balance",
            font=FONT_BODY_BOLD,
            height=35,
            command=self.refresh_ui_data,
            fg_color=self.current_theme["primary"]
        ).pack(fill="x", padx=15, pady=15)

    def create_summary_panel(self, parent):
        """Create summary statistics panel"""
        card = ctk.CTkFrame(parent, fg_color=self.current_theme["card"], corner_radius=10)
        card.pack(fill="both", expand=True, pady=10)
        
        ctk.CTkLabel(card, text="📈 Financial Summary", font=FONT_H2, text_color=self.current_theme["primary"]).pack(anchor="w", padx=15, pady=(15, 10))
        
        self.total_label = ctk.CTkLabel(card, text="💷 Total Spent: ₹0.00", font=FONT_BODY_BOLD, text_color=self.current_theme["text"])
        self.total_label.pack(anchor="w", padx=20, pady=5)
        
        self.remaining_label = ctk.CTkLabel(card, text="💰 Remaining: N/A", font=FONT_BODY_BOLD, text_color=self.current_theme["text"])
        self.remaining_label.pack(anchor="w", padx=20, pady=5)
        
        self.percentage_label = ctk.CTkLabel(card, text="📊 Spent: 0%", font=FONT_BODY_BOLD, text_color=self.current_theme["text"])
        self.percentage_label.pack(anchor="w", padx=20, pady=5)
        
        self.status_label = ctk.CTkLabel(card, text="ℹ️ Enter salary", font=FONT_BODY_BOLD, text_color=self.current_theme["primary"])
        self.status_label.pack(anchor="w", padx=20, pady=5)
        
        self.top_category_label = ctk.CTkLabel(card, text="🏆 Top Category: N/A", font=FONT_BODY_BOLD, text_color=self.current_theme["text"])
        self.top_category_label.pack(anchor="w", padx=20, pady=5)

    def create_expense_log(self, parent):
        """Create expense history table"""
        # Search Frame
        search_frame = ctk.CTkFrame(parent, fg_color="transparent")
        search_frame.pack(fill="x", padx=10, pady=(5, 0))
        
        ctk.CTkLabel(search_frame, text="🔍 Search:", font=FONT_SMALL_BOLD, text_color=self.current_theme["text"]).pack(side="left", padx=(0, 5))
        
        self.search_entry = ctk.CTkEntry(
            search_frame, 
            placeholder_text="Search categories or comments...",
            textvariable=self.search_var,
            height=30
        )
        self.search_entry.pack(side="left", fill="x", expand=True)
        
        ctk.CTkButton(
            search_frame,
            text="❌",
            width=30,
            height=30,
            command=self.clear_search,
            fg_color="transparent",
            hover_color=self.current_theme["bg"],
            text_color=self.current_theme["text"]
        ).pack(side="left", padx=(5, 0))

        # Treeview frame
        tree_frame = ctk.CTkFrame(parent, fg_color="transparent")
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Style for Treeview
        style = ttk.Style()
        style.theme_use('clam')
        
        bg_color = self.current_theme["card"]
        fg_color = self.current_theme["text"]
        
        style.configure('Treeview', 
                        background=bg_color, 
                        foreground=fg_color, 
                        fieldbackground=bg_color,
                        rowheight=30,
                        font=FONT_BODY)
        style.configure('Treeview.Heading', font=FONT_SMALL_BOLD, background=self.current_theme["primary"], foreground="white")
        style.map('Treeview', background=[('selected', self.current_theme["primary"])])
        
        self.tree = ttk.Treeview(
            tree_frame,
            columns=("Amount", "Category", "Comment", "Date"),
            show="headings"
        )
        
        self.tree.heading("Amount", text="Amount (₹)")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Comment", text="Comment")
        self.tree.heading("Date", text="Date & Time")
        
        self.tree.column("Amount", width=100, anchor="center")
        self.tree.column("Category", width=120, anchor="center")
        self.tree.column("Comment", width=250, anchor="w")
        self.tree.column("Date", width=150, anchor="center")
        
        # Add hidden Column for ID
        self.tree["columns"] = ("Amount", "Category", "Comment", "Date", "ID")
        self.tree.column("ID", width=0, stretch=False)
        self.tree["displaycolumns"] = ("Amount", "Category", "Comment", "Date")
        
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Delete Selected button
        ctk.CTkButton(
            parent,
            text="🗑️ Delete Selected Expense",
            font=FONT_BODY_BOLD,
            height=35,
            command=self.delete_expense,
            fg_color=self.current_theme["danger"],
            hover_color="#c0392b"
        ).pack(fill="x", padx=15, pady=15)

    def create_analysis_tab(self, parent):
        """Create the analysis tab with charts"""
        self.analysis_frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.analysis_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.chart_label = ctk.CTkLabel(self.analysis_frame, text="Expense Distribution", font=FONT_H2, text_color=self.current_theme["primary"])
        self.chart_label.pack(pady=(0, 10))
        
        self.chart_container = ctk.CTkFrame(self.analysis_frame, fg_color=self.current_theme["card"], corner_radius=10)
        self.chart_container.pack(fill="both", expand=True)
        
        self.no_data_label = ctk.CTkLabel(self.chart_container, text="No expense data to analyze.\nAdd some expenses first!", font=FONT_BODY)
        self.no_data_label.pack(expand=True)

    def create_status_bar(self, parent):
        """Create status bar at bottom"""
        status_frame = ctk.CTkFrame(parent, fg_color=self.current_theme["primary"], height=30)
        status_frame.pack(fill="x")
        status_frame.pack_propagate(False)
        
        self.status_message = ctk.CTkLabel(status_frame, text="✅ Ready", font=FONT_SMALL_BOLD, text_color="white")
        self.status_message.pack(anchor="w", padx=20, pady=5)

    def update_status(self, message, duration=3000):
        self.status_message.configure(text=message)
        self.root.after(duration, lambda: self.status_message.configure(text="✅ Ready"))

    def toggle_theme(self):
        """Toggle between dark and light mode"""
        self.dark_mode = not self.dark_mode
        ctk.set_appearance_mode("dark" if self.dark_mode else "light")
        self.current_theme = DARK_THEME if self.dark_mode else LIGHT_THEME
        
        # Save color selection if we had persistent settings (placeholder)
        
        # Hard refresh UI
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_ui()
        self.update_status(f"✅ {'Dark' if self.dark_mode else 'Light'} mode enabled")

    def refresh_ui_data(self):
        """Refresh all labels, table and charts"""
        # Load from entry
        salary_str = self.salary_entry.get().strip()
        try:
            self.salary = float(salary_str) if salary_str else 0.0
        except ValueError:
            messagebox.showwarning("⚠️ Warning", "Please enter a valid salary number.")
            self.salary = 0.0
            
        # Update labels
        metrics = calculate_financials(self.expenses, self.salary)
        
        self.total_label.configure(text=f"💷 Total Spent: ₹{metrics['total']:.2f}")
        
        if self.salary > 0:
            self.remaining_label.configure(text=f"💰 Remaining: ₹{metrics['remaining']:.2f}")
            self.percentage_label.configure(text=f"📊 Spent: {metrics['percentage']:.1f}%")
        else:
            self.remaining_label.configure(text="💰 Remaining: N/A")
            self.percentage_label.configure(text="📊 Spent: 0%")
            
        # Status styling
        status_color = self.current_theme["primary"]
        if metrics["status_type"] == "danger": status_color = self.current_theme["danger"]
        elif metrics["status_type"] == "warning": status_color = self.current_theme["warning"]
        elif metrics["status_type"] == "success": status_color = self.current_theme["secondary"]
        
        self.status_label.configure(text=metrics["status"], text_color=status_color)
        self.top_category_label.configure(text=f"🏆 Top Category: {metrics['top_category']}")
        
        # Refresh Table
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        search_term = self.search_var.get().lower()
        
        for exp in self.expenses:
            # Filter logic: Match Comment or Category
            match_comment = search_term in exp['comment'].lower()
            match_category = search_term in exp['category'].lower()
            
            if not search_term or match_comment or match_category:
                self.tree.insert("", "end", values=(f"₹{exp['expense']:.2f}", exp['category'], exp['comment'], exp['date'], exp['id']))
            
        # Refresh Chart
        self.update_chart()

    def update_chart(self):
        """Update the matplotlib chart in the analysis tab"""
        if self.chart_canvas:
            self.chart_canvas.get_tk_widget().destroy()
            self.chart_canvas = None
            
        if not self.expenses:
            self.no_data_label.pack(expand=True)
            return
            
        self.no_data_label.pack_forget()
        
        fig = generate_category_chart(self.expenses, self.dark_mode)
        if fig:
            self.chart_canvas = FigureCanvasTkAgg(fig, master=self.chart_container)
            self.chart_canvas.draw()
            self.chart_canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)
            plt.close(fig) # Prevent memory leaks

    def add_expense(self):
        """Validate and add a new expense"""
        amount_str = self.expense_entry.get().strip()
        category = self.category_combo.get()
        comment = self.comment_entry.get().strip()
        
        if not amount_str:
            messagebox.showwarning("⚠️ Input Error", "Amount is required!")
            return
            
        try:
            amount = float(amount_str)
            if amount <= 0: raise ValueError
        except ValueError:
            messagebox.showwarning("⚠️ Input Error", "Please enter a valid amount greater than 0.")
            return
            
        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        comment = comment if comment else "N/A"
        
        try:
            self.db.add_expense(amount, category, comment, date_str)
            self.load_data()
            self.refresh_ui_data()
            self.expense_entry.delete(0, "end")
            self.comment_entry.delete(0, "end")
            self.update_status(f"✅ Added ₹{amount:.2f} to {category}")
        except Exception as e:
            messagebox.showerror("❌ Database Error", str(e))

    def delete_expense(self):
        """Delete selected expense from table and database"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("⚠️ Selection Error", "Please select an expense to delete.")
            return
            
        if not messagebox.askyesno("🗑️ Confirm Delete", "Are you sure you want to delete the selected expense(s)?"):
            return
            
        try:
            for item in selection:
                expense_id = self.tree.item(item)['values'][4]
                self.db.delete_expense(expense_id)
            
            self.load_data()
            self.refresh_ui_data()
            self.update_status("✅ Deleted successfully")
        except Exception as e:
            messagebox.showerror("❌ Database Error", str(e))
            
    def clear_search(self):
        """Reset search entry and focus it"""
        self.search_var.set("")
        self.search_entry.focus()

if __name__ == "__main__":
    root = ctk.CTk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
