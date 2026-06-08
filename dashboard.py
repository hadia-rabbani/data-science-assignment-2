import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE CONFIG 
st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

# SIMPLE BACKGROUND STYLE 
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# LOAD DATA 
df = pd.read_csv("GlobalSuperstoreData.csv")
df.columns = df.columns.str.strip()
df = df.dropna()

# Convert date (safe)
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# HEADER 
st.title(" Sales Performance Dashboard")
st.write("A simple beginner-friendly dashboard for analyzing sales and profit data.")

st.markdown("---")

# SIDEBAR FILTERS
st.sidebar.header("Filters")

segment = st.sidebar.selectbox("Segment", df["Segment"].unique())
market = st.sidebar.selectbox("Market", df["Market"].unique())

# Filter data
filtered_df = df[
    (df["Segment"] == segment) &
    (df["Market"] == market)
]

# KPIs 
st.subheader("Summary")

col1, col2 = st.columns(2)

col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")

st.markdown("---")

# CHART 1
st.subheader(" Sales by Segment")

fig1 = px.bar(
    filtered_df,
    x="Segment",
    y="Sales",
    color="Segment"
)

st.plotly_chart(fig1, use_container_width=True)

# CHART 2
st.subheader(" Profit Analysis")

fig2 = px.bar(
    filtered_df,
    x="Segment",
    y="Profit",
    color="Market"
)

st.plotly_chart(fig2, use_container_width=True)

# RAW DATA (BEGINNER TOUCH) 
st.markdown("---")

if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)