# 💸 Expense Tracker Pro

A modern, professional desktop application to track your daily expenses, manage your budget, and visualize your spending patterns. Built with **CustomTkinter** for a sleek, contemporary UI.

## ✨ Features

✅ **Modern UI Design** - Built with CustomTkinter for professional look  
✅ **Dark/Light Mode Toggle** - Switch themes with one click  
✅ **Add Expenses** - Record expenses with amount, category dropdown, and comments  
✅ **Professional Treeview Table** - View all expenses in organized columns (Amount, Category, Comment, Date)  
✅ **Data Persistence** - Automatically saves expenses to JSON file  
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

- Expenses are automatically saved to `expenses_data.json`
- Data persists between application sessions
- JSON file is created in the same directory as the application
- No manual save required!

### Sample Data Format
```json
[
  {
    "expense": 150.50,
    "category": "Food",
    "comment": "Lunch at restaurant",
    "date": "2025-11-17 14:30"
  },
  {
    "expense": 500.00,
    "category": "Transport",
    "comment": "Monthly fuel",
    "date": "2025-11-17 09:15"
  }
]
```

## 📁 File Structure

```
expense-tracker/
│
├── __init__.py              # Main application file (CustomTkinter implementation)
├── expenses_data.json       # Auto-generated data file (created on first use)
├── README.md               # Documentation (this file)
└── .gitignore             # Exclude unnecessary files from version control
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

### ❌ JSON file corrupted
- Delete `expenses_data.json`
- Restart the application
- A fresh file will be automatically created

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
