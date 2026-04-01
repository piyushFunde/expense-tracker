import sqlite3
import os
import json
from tkinter import messagebox

class DatabaseManager:
    def __init__(self, db_file="expenses.db", data_file="expenses_data.json"):
        self.db_file = db_file
        self.data_file = data_file
        self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        """Initialize SQLite database and migrate JSON data if necessary"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expense REAL NOT NULL,
                category TEXT NOT NULL,
                comment TEXT,
                date TEXT NOT NULL
            )
        ''')
        self.conn.commit()
        
        # Migrate from JSON if it exists
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    json_data = json.load(file)
                    for item in json_data:
                        self.cursor.execute('''
                            INSERT INTO expenses (expense, category, comment, date)
                            VALUES (?, ?, ?, ?)
                        ''', (item['expense'], item['category'], item['comment'], item['date']))
                self.conn.commit()
                # Backup and rename JSON file
                os.rename(self.data_file, self.data_file + ".bak")
                return True, "Successfully migrated data to database."
            except Exception as e:
                return False, f"Failed to migrate data: {str(e)}"
        return None, None

    def load_expenses(self):
        """Load expenses from database"""
        try:
            self.cursor.execute('SELECT id, expense, category, comment, date FROM expenses ORDER BY date DESC')
            rows = self.cursor.fetchall()
            expenses = []
            for row in rows:
                expenses.append({
                    "id": row[0],
                    "expense": row[1],
                    "category": row[2],
                    "comment": row[3],
                    "date": row[4]
                })
            return expenses
        except Exception as e:
            raise Exception(f"Failed to load expenses: {str(e)}")

    def add_expense(self, expense, category, comment, date):
        """Add a new expense to the database"""
        try:
            self.cursor.execute('''
                INSERT INTO expenses (expense, category, comment, date)
                VALUES (?, ?, ?, ?)
            ''', (expense, category, comment, date))
            self.conn.commit()
            return True
        except Exception as e:
            raise Exception(f"Failed to save expense: {str(e)}")

    def delete_expense(self, expense_id):
        """Delete an expense by ID"""
        try:
            self.cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
            self.conn.commit()
            return True
        except Exception as e:
            raise Exception(f"Failed to delete expense: {str(e)}")

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()
