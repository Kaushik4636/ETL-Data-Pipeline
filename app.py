import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="ETL Pipeline Pro", page_icon="⚙️")
st.title("⚙️ Automated ETL Pipeline")
st.write("Upload a CSV to transform data and load it into a SQLite Database.")

# --- ETL Functions ---

def transform(data):
    # Standardize department names to uppercase
    if 'department' in data.columns:
        data['department'] = data['department'].str.upper()
        # Give a 10% raise to Engineering
        if 'salary' in data.columns:
            data.loc[data['department'] == 'ENGINEERING', 'salary'] *= 1.10
    return data

def load_to_sqlite(data):
    db_file = "transformed_data.db"
    conn = sqlite3.connect(db_file)
    data.to_sql('employees', conn, if_exists='replace', index=False)
    conn.close()
    return db_file

# --- UI Layout ---

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # 1. EXTRACT
    df = pd.read_csv(uploaded_file)
    st.subheader("1. Extracted Data (Raw)")
    st.dataframe(df.head())

    # 2. TRANSFORM
    if st.button("Run Transformation"):
        transformed_df = transform(df)
        st.subheader("2. Transformed Data")
        st.write("Action: Uppercased departments & applied Engineering salary bonus.")
        st.dataframe(transformed_df.head())

        # 3. LOAD
        db_path = load_to_sqlite(transformed_df)
        st.success(f"3. Data loaded into {db_path} successfully!")

        # Download button for the database file
        with open(db_path, "rb") as f:
            st.download_button(
                label="Download SQLite Database",
                data=f,
                file_name="employees_database.db",
                mime="application/x-sqlite3"
            )
else:
    st.info("Please upload the 'employees.csv' file to start the pipeline.")