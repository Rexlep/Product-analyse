import pandas as pd

# Sample data with datetime
data = {
    'Date': ['2024-01-15', '2024-01-20', '2024-02-10', '2024-02-15', '2024-03-05'],
    'Sales_Count': [4, 8, 5, 7, 3]
}

df = pd.DataFrame(data)

# Convert 'Date' column to datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Extract month name
df['Month'] = df['Date'].dt.month_name()  # or use .dt.month for numeric month

# Group by month and sum sales
monthly_sales = df.groupby('Month')['Sales_Count'].sum()

# Check and print message for months with sales > 10
for month, total in monthly_sales.items():
    if total > 10:
        print(f"In {month}, high total sales were recorded ({total} items)")
