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
        
        column_type = df[selected_column].dtype
        if column_type in ['int64', 'float64']:
            st.subheader("Numerical Column Analysis: " + selected_column)

            summary_table = df[selected_column].describe()
            st.write("Five Number Summary:")
            st.write(summary_table)

            st.write("Box Plot:")
            fig, ax = plt.subplots()
            sns.boxplot(data=df, y=selected_column)
            ax.set_ylabel(selected_column)
            st.pyplot(fig)

        elif column_type == 'object':
            st.subheader("Categorical Column Analysis: " + selected_column)

            category_proportions = df[selected_column].value_counts(
                normalize=True)
            st.write("Proportions of Each Category Level:")
            st.write(category_proportions)

            st.write("Bar Plot:")
            fig, ax = plt.subplots()
            sns.countplot(data=df, x=selected_column)
            ax.set_xlabel(selected_column)
            ax.set_ylabel("Count")
            st.pyplot(fig)

elif web_apps == "Correlation":

    if df is None:
        uploaded_file = st.file_uploader("Upload a file for correlation analysis")

        if uploaded_file is not None:
            # Can be used wherever a "file-like" object is accepted:
            df = pd.read_csv(uploaded_file)

