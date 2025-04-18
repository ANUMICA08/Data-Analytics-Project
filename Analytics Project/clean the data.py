import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_excel(r"C:\Users\K.S.Abilesh\Downloads\Online Retail.xlsx")

# Clean Data
df = df[df['CustomerID'].notnull()]
df = df[df['Quantity'] > 0]
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Feature Engineering
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
df['YearMonth'] = df['InvoiceDate'].dt.to_period('M')
df['Day'] = df['InvoiceDate'].dt.day
df['Hour'] = df['InvoiceDate'].dt.hour

# Analysis
total_revenue = df['TotalPrice'].sum()
top_products = df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)
country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)

# Visualization
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Top 10 Products by Revenue')
plt.show()

# Info
print(df.shape)
print(df.head())

# ✅ Save cleaned data
df.to_csv(r"C:\Users\K.S.Abilesh\Downloads\cleaned_online_retail.csv", index=False)








