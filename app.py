import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

web_apps = st.sidebar.selectbox("Select Web Apps",
                                ("Exploratory Data Analysis", "Distributions", "Correlation"))

df = None  # Define df variable

if web_apps == "Exploratory Data Analysis":

    uploaded_file = st.sidebar.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        df = pd.read_csv(uploaded_file)
        show_df = st.checkbox("Show Data Frame", key="disabled")

        if show_df:
            st.write(df)

        num_rows = df.shape[0]
        num_columns = df.shape[1]
        num_categorical = len(df.select_dtypes(include=['object']).columns)
        num_numerical = len(df.select_dtypes(
            include=['int64', 'float64']).columns)
        num_boolean = len(df.select_dtypes(include=['bool']).columns)

        st.subheader("Dataset Statistics")
        st.write("Number of rows:", num_rows)
        st.write("Number of columns:", num_columns)
        st.write("Number of categorical variables:", num_categorical)
        st.write("Number of numerical variables:", num_numerical)
        st.write("Number of boolean variables:", num_boolean)

        selected_column = st.sidebar.selectbox("Select a Column", df.columns)
