import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_context("talk")
palette = sns.color_palette("Set2")

df = pd.read_csv("ecommerce_dataset.csv")

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Month'] = df['OrderDate'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('Month')['TotalPrice'].sum().reset_index()

top_products = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False).reset_index()

country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).reset_index()

payment_sales = df.groupby('PaymentMethod')['TotalPrice'].sum().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(data=monthly_sales, x='Month', y='TotalPrice', marker='o', color='blue')
plt.title(" Monthly Sales Trend", fontsize=16, fontweight='bold')
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Revenue")

for i, value in enumerate(monthly_sales['TotalPrice']):
    plt.text(i, value, str(round(value, 0)), ha='center', fontsize=8)

plt.tight_layout()
plt.savefig("sales_trend.png")
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(data=top_products.head(10), x='TotalPrice', y='Product', palette='viridis')
plt.title(" Top 10 Products by Revenue", fontsize=16, fontweight='bold')

for index, value in enumerate(top_products.head(10)['TotalPrice']):
    plt.text(value, index, str(round(value, 0)))

plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(data=country_sales, x='Country', y='TotalPrice', palette='coolwarm')
plt.title(" Revenue by Country", fontsize=16, fontweight='bold')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("country_sales.png")
plt.show()

plt.figure(figsize=(7,7))

colors = sns.color_palette('pastel')

plt.pie(payment_sales['TotalPrice'],
        labels=payment_sales['PaymentMethod'],
        autopct='%1.1f%%',
        colors=colors,
        wedgeprops={'width':0.4})

plt.title(" Payment Method Distribution", fontsize=16, fontweight='bold')

plt.savefig("payment_method.png")
plt.show()










