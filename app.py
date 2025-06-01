import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sample_sales_data.csv')

st.title("Sales Performance Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
regions = df['Region'].unique()
categories = df['Category'].unique()

selected_region = st.sidebar.multiselect("Select Region(s)", options=regions, default=regions)
selected_category = st.sidebar.multiselect("Select Category(s)", options=categories, default=categories)

# Filter data based on selections
filtered_df = df[(df['Region'].isin(selected_region)) & (df['Category'].isin(selected_category))]

st.write("### Filtered Data", filtered_df)

# Summary stats
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_discount = filtered_df['Discount'].sum()

st.markdown(f"**Total Sales:** ₹{total_sales:,.2f}  \n**Total Profit:** ₹{total_profit:,.2f}  \n**Total Discount:** ₹{total_discount:,.2f}")

# Sales by Region bar chart
st.subheader("Sales by Region")
region_sales = filtered_df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
st.bar_chart(region_sales)

# Profit by Category pie chart
st.subheader("Profit by Category")
cat_profit = filtered_df.groupby('Category')['Profit'].sum()
fig1, ax1 = plt.subplots()
ax1.pie(cat_profit, labels=cat_profit.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
ax1.axis('equal')
st.pyplot(fig1)

# Discount by Category bar chart
st.subheader("Average Discount by Category")
cat_discount = filtered_df.groupby('Category')['Discount'].mean()
st.bar_chart(cat_discount)

