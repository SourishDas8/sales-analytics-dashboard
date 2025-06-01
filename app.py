import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Sales Performance Dashboard", layout="wide")

# Load data
df = pd.read_csv('sample_sales_data.csv')

# Title
st.title("📊 Sales Performance Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
regions = df['Region'].unique()
categories = df['Category'].unique()

selected_region = st.sidebar.multiselect("Select Region(s):", options=regions, default=regions)
selected_category = st.sidebar.multiselect("Select Category(s):", options=categories, default=categories)

# Filter data based on selections
filtered_df = df[(df['Region'].isin(selected_region)) & (df['Category'].isin(selected_category))]

# Show filtered data
st.markdown("### Filtered Sales Data")
st.dataframe(filtered_df.reset_index(drop=True))

# Summary KPIs
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
avg_discount = filtered_df['Discount'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"₹{total_sales:,.2f}")
col2.metric("📈 Total Profit", f"₹{total_profit:,.2f}")
col3.metric("🏷️ Average Discount", f"{avg_discount:.2f}%")

st.markdown("---")

# Sales by Region
st.subheader("Sales by Region")
region_sales = filtered_df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
fig1, ax1 = plt.subplots()
region_sales.plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_ylabel("Sales (₹)")
ax1.set_xlabel("Region")
ax1.set_title("Total Sales by Region")
st.pyplot(fig1)

# Profit by Category Pie Chart
st.subheader("Profit Distribution by Category")
cat_profit = filtered_df.groupby('Category')['Profit'].sum()
fig2, ax2 = plt.subplots()
ax2.pie(cat_profit, labels=cat_profit.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
ax2.axis('equal')
st.pyplot(fig2)

# Discount by Category Bar Chart
st.subheader("Average Discount by Category")
cat_discount = filtered_df.groupby('Category')['Discount'].mean()
fig3, ax3 = plt.subplots()
cat_discount.plot(kind='bar', ax=ax3, color='coral')
ax3.set_ylabel("Average Discount (%)")
ax3.set_xlabel("Category")
ax3.set_title("Average Discount Percentage by Category")
st.pyplot(fig3)

# Optional: Sales Trend by Date if you have date column
if 'Order Date' in df.columns:
    st.subheader("Sales Trend Over Time")
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    filtered_date_df = df[(df['Region'].isin(selected_region)) & (df['Category'].isin(selected_category))]
    sales_trend = filtered_date_df.groupby('Order Date')['Sales'].sum()
    fig4, ax4 = plt.subplots()
    sales_trend.plot(ax=ax4, color='green')
    ax4.set_ylabel("Sales (₹)")
    ax4.set_xlabel("Date")
    ax4.set_title("Sales Trend Over Time")
    st.pyplot(fig4)

# Footer
st.markdown("---")
st.markdown("Developed by **Your Name** | Data Analytics Portfolio Project")
