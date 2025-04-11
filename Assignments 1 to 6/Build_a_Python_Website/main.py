
from matplotlib.pylab import unique_values
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_colum = st.selectbox("Select column to filter by", columns)

    unique_column = df[selected_colum].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df= df[df[selected_colum] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

    else:
        st.write("Waiting on file upload...")
