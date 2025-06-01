import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sample_sales_data.csv')
st.title("Sales Performance Dashboard")
st.write(df.head())

# Region-wise sales
st.subheader("Sales by Region")
region_sales = df.groupby('Region')['Sales'].sum()
st.bar_chart(region_sales)

# Category Profit Pie
st.subheader("Profit by Category")
cat_profit = df.groupby('Category')['Profit'].sum()
st.write(cat_profit.plot(kind='pie', autopct='%1.1f%%'))
st.pyplot(plt.gcf())
