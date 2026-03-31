# 💸 Expense Tracker Pro

A modern, professional desktop application to track your daily expenses, manage your budget, and visualize your spending patterns. Built with **CustomTkinter** for a sleek, contemporary UI.

## ✨ Features

✅ **Modern UI Design** - Built with CustomTkinter for professional look  
✅ **Dark/Light Mode Toggle** - Switch themes with one click  
✅ **Add Expenses** - Record expenses with amount, category dropdown, and comments  
✅ **Professional Treeview Table** - View all expenses in organized columns (Amount, Category, Comment, Date)  
✅ **Data Persistence** - Automatically saves expenses to a robust **SQLite database**  
✅ **Budget Tracking** - Compare expenses against your salary  
✅ **Financial Summary Panel** - Shows total, remaining, percentage, status, and top category  
✅ **Real-time Calculations** - Instant total expense and remaining balance updates  
✅ **Status Bar** - Real-time notifications for all actions  
✅ **Color-Coded Status** - Visual feedback on budget health  
✅ **Timestamp Logging** - Auto-timestamp for every transaction  
✅ **Category Dropdown** - Select from pre-defined categories  
✅ **Responsive Layout** - Two-column design that adapts to window size  
✅ **Interactive Buttons** - Hover effects on all buttons  

## 📋 Installation

### Requirements
- Python 3.7 or higher
- CustomTkinter
- tkinter (included with Python)


## 🚀 Usage

### Running the Application

```bash
python __init__.py
```

Or with Python 3:
```bash
python3 __init__.py
```

### How to Use

#### 1️⃣ **Add Expense**
   - Enter the amount in rupees (₹)
   - Select a category from the dropdown menu
   - Add optional comments/notes
   - Click "➕ Add Expense"
   - Expense automatically saves and appears in the table

#### 2️⃣ **Track Budget**
   - Enter your monthly salary in "Salary Information" section
   - Click "📊 Calculate Total"
   - View comprehensive financial summary:
     - 💷 Total Expenses
     - 💰 Remaining Balance
     - 📊 Spending Percentage
     - 🏆 Top Spending Category
   - Status indicator shows budget health:
     - 🟢 **Green (Healthy)** - More than 20% remaining
     - 🟠 **Orange (Low)** - Between 0-20% remaining
     - 🔴 **Red (Over Budget)** - Overspent

#### 3️⃣ **Manage Expenses**
   - View all expenses in the Treeview table with columns:
     - **Amount (₹)** - Transaction amount
     - **Category** - Expense category
     - **Comment** - Notes/description
     - **Date & Time** - Transaction timestamp
   - Select an expense from the table
   - Click "🗑️ Delete Selected" to remove it
   - Changes automatically saved

#### 4️⃣ **Toggle Theme**
   - Click "🌙 Dark Mode" button in header to switch themes
   - App saves preference for next session
   - Choose between Light and Dark modes

## 💾 Data Storage

- Expenses are automatically saved to an **SQLite database** (`expenses.db`)
- Data persists between application sessions with high reliability
- **Migration**: On first run, the app automatically migrates data from `expenses_data.json` to the new database
- **Security**: Database operations are atomic and protected against corruption
- No manual save required!

### Database Schema
| Column | Type | Description |
|---|---|---|
| **id** | INTEGER | Primary Key (Auto-increment) |
| **expense** | REAL | Transaction amount |
| **category** | TEXT | Expense category |
| **comment** | TEXT | Optional notes |
| **date** | TEXT | ISO Format timestamp |

## 📁 File Structure

```
expense-tracker/
│
├── __init__.py              # Main application file (CustomTkinter implementation)
├── expenses.db              # SQLite Database (auto-generated)
├── README.md               # Documentation (this file)
└── .gitignore             # Excludes database and private files from GitHub
```

## 🎨 UI Components

### Header
- **Title**: 💸 Expense Tracker Pro
- **Subtitle**: "Manage your finances with ease"
- **Theme Toggle**: 🌙 Dark Mode button (top-right)

### Two-Column Layout
**Left Column:**
1. **📝 Add New Expense** (Card)
   - Amount input field
   - Category dropdown menu
   - Comment input field
   - Add Expense button

2. **💰 Salary Information** (Card)
   - Salary input field
   - Calculate Total button

3. **📈 Financial Summary** (Card)
   - Total Expenses
   - Remaining Balance
   - Spending Percentage
   - Budget Status
   - Top Category

**Right Column:**
4. **📋 Expense History** (Card)
   - Professional Treeview table with 4 columns
   - Scrollable list of all expenses
   - Delete Selected button

### Status Bar
- **Bottom**: Real-time notifications and status messages
- Shows actions like "✅ Added ₹150 to Food"
- Auto-resets to "✅ Ready" after 3 seconds

## 🌈 Theme Modes

### Light Mode (Default)
- Clean white cards
- Professional blue primary color
- Easy on the eyes
- Great for daytime use

### Dark Mode
- Dark gray cards on dark background
- Reduced eye strain
- Perfect for night use
- All colors optimized for dark theme

## 🎯 Default Expense Categories

- 🍔 **Food** - Restaurants, groceries
- 🚗 **Transport** - Fuel, public transport, taxi
- 🏠 **Housing** - Rent, utilities, maintenance
- 🎮 **Entertainment** - Movies, games, music
- 💊 **Health** - Medicine, doctor visits, gym
- 📚 **Education** - Books, courses, training
- 👕 **Shopping** - Clothes, accessories, gifts
- 🔧 **Utilities** - Bills, subscriptions, repairs
- 🎯 **Other** - Miscellaneous expenses

## 🔧 Troubleshooting

### ❌ "No module named 'customtkinter'"
```bash
# Install CustomTkinter
pip install customtkinter

# Or upgrade if already installed
pip install --upgrade customtkinter
```

### ❌ Application won't start
```bash
# Verify Python installation
python --version

# Ensure you're in correct directory
cd "c:\Users\PROGRAMING FILE\expense-tracker"

# Try running with explicit Python 3
python3 __init__.py
```

### ❌ Database Error
- Ensure you have write permissions in the project folder
- Check if `expenses.db` is being used by another application
- If migration failed, check `expenses_data.json.bak` for your original data

### ❌ Resetting the Application
- Delete `expenses.db` to start with a fresh database
- If you have an old `expenses_data.json`, the app will attempt to re-migrate it

### ❌ Data not saving
- Check folder permissions (right-click → Properties)
- Ensure enough disk space
- Try running as Administrator
- Check if antivirus is blocking file access

### ❌ Treeview table not showing expenses
- Click "📊 Calculate Total" to refresh
- Verify expenses in `expenses_data.json`
- Try restarting the application

### ❌ Theme toggle not working
- Restart the application
- Verify CustomTkinter is properly installed
- Check Python version (3.7+)

## 📊 Color Coding

| Status | Color | Meaning |
|---|---|---|
| 🟢 Healthy | Green | >20% of salary remaining |
| 🟠 Low Budget | Orange | 0-20% of salary remaining |
| 🔴 Over Budget | Red | Negative balance (overspent) |
| ℹ️ No Salary | Gray | Enter salary for analysis |

## 🚀 Future Enhancements

🔄 **Planned Features:**
- ✏️ Edit existing expenses (double-click to edit)
- 📅 Filter by date range or category
- 📊 Export reports to CSV/PDF
- 📈 Statistics dashboard with pie/bar charts
- 🎯 Monthly budget limits and alerts
- 🔁 Recurring expense templates
- 👥 Multi-user support
- 🔐 Password protection
- 💾 Cloud backup integration
- 📱 Mobile app version

## ⚙️ System Requirements

| Requirement | Specification |
|---|---|
| **Python** | 3.7 or higher |
| **OS** | Windows, macOS, Linux |
| **RAM** | 100MB minimum |
| **Disk Space** | 2MB minimum |
| **Display** | 900x650 minimum resolution |
| **Dependencies** | customtkinter, tkinter (built-in) |

## 📝 License

This project is open source and free to use for personal and educational purposes.

## 👨‍💻 Author

Created as a modern personal finance management tool using Python and CustomTkinter.

## 🆘 Support & Issues

For issues or suggestions:
1. Check the **Troubleshooting** section above
2. Review the code in `__init__.py`
3. Check [CustomTkinter documentation](https://github.com/TomSchimansky/CustomTkinter)
4. Verify your Python installation
5. Ensure CustomTkinter is properly installed: `pip list | grep customtkinter`

## 📞 Quick Tips

💡 **Tip 1**: Keep your salary updated for accurate budget tracking  
💡 **Tip 2**: Use descriptive comments to remember expense details  
💡 **Tip 3**: Review your top spending category regularly  
💡 **Tip 4**: Toggle between light/dark mode based on your preference  
💡 **Tip 5**: Backup your `expenses_data.json` file regularly  
💡 **Tip 6**: Use the status bar to confirm successful actions  
