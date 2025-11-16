
# 💸 Expense Tracker

A simple and intuitive desktop application to track your daily expenses, manage your budget, and visualize your spending patterns.

## ✨ Features

✅ **Add Expenses** - Record expenses with amount, category, and comments  
✅ **Data Persistence** - Automatically saves expenses to JSON file  
✅ **Budget Tracking** - Compare expenses against your salary  
✅ **Color-Coded Status** - Visual feedback on remaining balance  
✅ **Delete Expenses** - Remove unwanted expense entries  
✅ **Real-time Calculations** - Instant total expense and remaining balance updates  
✅ **Timestamp Logging** - Auto-timestamp for every transaction  

## 📋 Installation

### Requirements
- Python 3.7 or higher
- tkinter (included with Python)

### Setup

1. **Navigate to project folder:**
```bash
cd c:\Users\funde\OneDrive\Pictures\Documents\Documents\PROGRAMING FILE\expense-tracker
```

2. **No additional dependencies required!**
   - tkinter comes built-in with Python
   - Uses only standard library modules (json, datetime, os)

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
   - Select a category (e.g., Food, Transport, Entertainment)
   - Add optional comments
   - Click "➕ Add Expense"
   - Expense automatically saves to file

#### 2️⃣ **Track Budget**
   - Enter your monthly salary in "Salary Info" section
   - Click "📊 Calculate Total"
   - View total expenses and remaining balance
   - Balance color changes based on status:
     - 🟢 **Green** - More than 20% remaining (Healthy)
     - 🟠 **Orange** - Between 0-20% remaining (Low)
     - 🔴 **Red** - Overspent (Over budget)

#### 3️⃣ **Manage Expenses**
   - Select an expense from the "Expense Log" list
   - Click "🗑️ Delete Selected" to remove it
   - Changes automatically saved

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
    "date": "2025-11-16 14:30"
  },
  {
    "expense": 500.00,
    "category": "Transport",
    "comment": "Monthly fuel",
    "date": "2025-11-16 09:15"
  }
]
```

## 📁 File Structure

```
expense-tracker/
│
├── __init__.py              # Main application file
├── expenses_data.json       # Auto-generated data file (created on first use)
├── README.md               # Documentation (this file)
└── .gitignore             # (Optional) Exclude data files from version control
```

## 🎨 UI Components

### Main Window
- **Title**: 💸 Expense Tracker
- **Size**: 500x600 pixels
- **Theme**: Light gray background (#f7f7f7)

### Sections
1. **Add Expense** (Green frame)
   - Amount input
   - Category input
   - Comments input
   - Add button

2. **Salary Info** (Blue frame)
   - Salary input
   - Calculate button

3. **Total Display**
   - Shows total expenses and remaining balance
   - Color-coded (Green/Orange/Red)

4. **Expense Log** (White frame)
   - Scrollable list of all expenses
   - Delete button below list

## 🔧 Troubleshooting

### ❌ Application won't start
```bash
# Verify Python installation
python --version

# Ensure you're in correct directory
cd "c:\Users\funde\OneDrive\Pictures\Documents\Documents\PROGRAMING FILE\expense-tracker"

# Try running with explicit Python 3
python3 __init__.py
```

### ❌ "ModuleNotFoundError: No module named 'tkinter'"
```bash
# Windows - Reinstall Python with tkinter option
# Or install via pip
pip install tk
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

### ❌ Numbers showing as text instead of calculations
- Ensure you enter valid numbers (123.45)
- Avoid special characters or letters
- Use decimal point (.) not comma (,)

## 📊 Color Coding Explained

| Balance Status | Color | Meaning |
|---|---|---|
| > 20% remaining | 🟢 Green | Healthy budget, spend wisely |
| 0-20% remaining | 🟠 Orange | Low budget, be careful |
| Negative | 🔴 Red | Over budget, exceeded salary |
| No salary set | ⚫ Gray | Just tracking expenses |

## 🎯 Expense Categories (Suggestions)

- 🍔 **Food** - Restaurants, groceries
- 🚗 **Transport** - Fuel, public transport
- 🏠 **Housing** - Rent, utilities
- 🎮 **Entertainment** - Movies, games
- 💊 **Health** - Medicine, doctor visits
- 📚 **Education** - Books, courses
- 👕 **Shopping** - Clothes, accessories
- 💰 **Savings** - Deposits, investments
- 📱 **Communication** - Phone bills, internet

## 🚀 Future Enhancements (Planned)

🔄 **Upcoming Features:**
- ✏️ Edit existing expenses
- 📅 Filter by date range or category
- 📊 Export reports to CSV/PDF
- 📈 Statistics dashboard with pie charts
- 🎯 Monthly budget limits and alerts
- 🔁 Recurring expense templates
- 👥 Multi-user support
- 🌙 Dark mode theme
- 🔐 Password protection
- 💬 Expense notes/receipts

## ⚙️ System Requirements

| Requirement | Specification |
|---|---|
| **Python** | 3.7 or higher |
| **OS** | Windows, macOS, Linux |
| **RAM** | 50MB minimum |
| **Disk Space** | 1MB minimum |
| **Display** | 800x600 minimum resolution |
| **Dependencies** | None (tkinter included with Python) |

## 📝 License

This project is open source and free to use for personal and educational purposes.

## 👨‍💻 Author

Created as a personal finance management tool.

## 🆘 Support & Issues

For issues or suggestions:
1. Check the **Troubleshooting** section above
2. Review the code in `__init__.py`
3. Check Python's [tkinter documentation](https://docs.python.org/3/library/tkinter.html)
4. Verify your Python installation

## 📞 Quick Tips

💡 **Tip 1**: Keep your salary updated for accurate balance tracking  
💡 **Tip 2**: Use clear category names for better organization  
💡 **Tip 3**: Add comments to remember expense details  
💡 **Tip 4**: Review your expenses regularly for spending patterns  
💡 **Tip 5**: Backup your `expenses_data.json` file regularly  

---

**Version**: 1.0  
**Last Updated**: November 16, 2025  
**Status**: Active Development ✅
