# csv2excel.py
import pandas as pd
import os

# CSV file path
csv_path = os.path.join("Data", "data.csv")

# Excel output path
excel_path = os.path.join("Data", "data.xlsx")

# 1 Read CSV
df = pd.read_csv(csv_path)

# 2 Data Cleaning
# Remove empty rows
df.dropna(how='all', inplace=True)

# 3 Export to Excel
df.to_excel(excel_path, index=False)

print(f"CSV has been successfully imported to Excel: {excel_path}")