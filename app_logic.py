import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

# Set non-interactive backend for thread safety
matplotlib.use('Agg')

def calculate_financials(expenses, salary):
    """Calculate financial metrics based on expenses and salary"""
    total_expense = sum(item['expense'] for item in expenses)
    remaining = salary - total_expense
    percentage = (total_expense / salary) * 100 if salary > 0 else 0
    
    # Status calculations
    if salary <= 0:
        status = "ℹ️ Enter salary"
        status_type = "info"
    elif remaining < 0:
        status = "🔴 OVER BUDGET"
        status_type = "danger"
    elif remaining < salary * 0.20:
        status = "🟠 LOW BUDGET"
        status_type = "warning"
    else:
        status = "🟢 HEALTHY"
        status_type = "success"
        
    # Top Category
    top_cat = "N/A"
    if expenses:
        category_sum = {}
        for expense in expenses:
            cat = expense['category']
            category_sum[cat] = category_sum.get(cat, 0) + expense['expense']
        
        if category_sum:
            top_cat_name = max(category_sum, key=category_sum.get)
            top_cat = f"{top_cat_name} (₹{category_sum[top_cat_name]:.2f})"
            
    return {
        "total": total_expense,
        "remaining": remaining,
        "percentage": percentage,
        "status": status,
        "status_type": status_type,
        "top_category": top_cat
    }

def generate_category_chart(expenses, is_dark_mode=False):
    """Generate a pie chart for expenses by category"""
    if not expenses:
        return None
    
    category_sum = {}
    for expense in expenses:
        cat = expense['category']
        category_sum[cat] = category_sum.get(cat, 0) + expense['expense']
    
    labels = list(category_sum.keys())
    sizes = list(category_sum.values())
    
    # Styling
    plt.style.use('dark_background' if is_dark_mode else 'default')
    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
    fig.patch.set_facecolor('#2d2d2d' if is_dark_mode else '#ffffff')
    
    colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6', '#1abc9c', '#34495e', '#e67e22']
    
    wedges, texts, autotexts = ax.pie(
        sizes, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=140,
        colors=colors,
        textprops={'color': 'white' if is_dark_mode else 'black'}
    )
    
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    return fig
