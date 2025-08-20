import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# --- 1. BAR CHART: Marks per Student ---

# Simulated students.csv content
csv_data = """
Name,Math,Science,English
Alice,85,78,92
Bob,90,NaN,88
Charlie,NaN,65,70
David,75,80,85
Eva,88,77,NaN
"""

# Read into DataFrame
df = pd.read_csv(StringIO(csv_data))

# Fill missing values (optional: use mean or 0)
df.fillna(0, inplace=True)

# Plot bar chart: each student's total marks
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Total'], color='skyblue')
plt.title("Total Marks per Student")
plt.xlabel("Student")
plt.ylabel("Total Marks")
plt.ylim(0, 300)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

#Monthly Sales Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1200, 1500, 1600, 1800, 2000, 2400,
         2200, 2100, 2300, 2500, 2700, 3000]

# Plot line chart
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='green')
plt.title("Monthly Sales of Company")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()