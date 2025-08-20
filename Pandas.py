import pandas as pd
from io import StringIO

# Simulated CSV content
csv_data = """
Name,Math,Science,English
Alice,85,78,92
Bob,90,,88
Charlie,NaN,65,70
David,75,80,85
Eva,88,77,NaN
"""

# Load the data
df = pd.read_csv(StringIO(csv_data))

# Clean the data: convert columns to numeric (if not already), and handle NaNs
df[['Math', 'Science', 'English']] = df[['Math', 'Science', 'English']].apply(pd.to_numeric, errors='coerce')

# Print the cleaned DataFrame (optional)
print("Cleaned Data:")
print(df)

# Compute average marks per subject (ignoring NaN)
average_marks = df[['Math', 'Science', 'English']].mean()

print("\nAverage Marks per Subject:")
print(average_marks)
