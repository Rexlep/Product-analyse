from datetime import datetime
import pandas as pd

df = pd.read_csv('products.csv')

timestamps = df['date']

for i in timestamps:
    dt = datetime.strptime(i, "%Y-%m-%d %H:%M:%S")
    only_date = dt.date()  # فقط تاریخ
    print(only_date)  # خروجی: 2012-12-12
