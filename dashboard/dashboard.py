import streamlit as st
import duckdb
import pandas as pd

def create_dashboard():
    # Read the Parquet file directly into a pandas DataFrame
    df = duckdb.query("SELECT * FROM 'data/measurements.parquet'").df()

    # Display the data as a table
    st.title("Weather Station Measurements")
    st.dataframe(df)

if __name__ == "__main__":
    create_dashboard()