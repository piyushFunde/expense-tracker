#Expense Tracker Pro

A modern, professional desktop application to track your daily expenses, manage your budget, and visualize your spending patterns. Built with **CustomTkinter** for a sleek, contemporary UI and **Matplotlib** for data analysis.

##Features

**Modern UI Design** - Refactored for better performance and modularity.  
**Interactive Charts** - New "Analysis" tab with category distribution pie charts.  
**Modular Architecture** - Cleanly separated logic, styles, and database operations.  
**Dark/Light Mode Toggle** - Switch themes and charts adapt automatically.  
**Professional Treeview Table** - View all expenses in organized columns.  
**SQLite Database** - Robust data persistence with automatic JSON migration.  
**Budget Tracking** - Real-time metrics for total spent, remaining balance, and status.  

## Installation

### Requirements
- Python 3.7 or higher
- CustomTkinter
- Matplotlib
- tkinter (included with Python)

### Quick Install
```bash
pip install -r requirements.txt
```

##  Usage

### Running the Application
```bash
python main.py
```

### How to Use
1. **Add Expense**: Enter amount, select category, and add an optional note.
2. **Track Budget**: Enter your monthly salary to see health indicators and remaining balance.
3. **Analyze**: Switch to the ** Analysis** tab to see a visual breakdown of your spending.
4. **Manage**: Use the ** History** tab to review or delete past transactions.

## Data Storage
- Expenses are saved in `expenses.db` (SQLite).
- On first run, old `expenses_data.json` files are automatically migrated.

##  File Structure
```
expense-tracker/
├── main.py          # Main application entry point & UI
├── database.py      # SQLite database manager
├── app_logic.py     # Calculations and chart generation logic
├── styles.py        # Centralized theme and font configurations
├── requirements.txt # Project dependencies
├── README.md        # Documentation
└── expenses.db      # SQLite Database (auto-generated)
```

## Refactoring Highlights
This project has been modularized to separate concerns:
- **`database.py`**: Encapsulates all CRUD operations.
- **`app_logic.py`**: Pure functions for math and visualization, making it testable.
- **`styles.py`**: easy-to-change theme constants.

---
Created as a modern personal finance management tool.
