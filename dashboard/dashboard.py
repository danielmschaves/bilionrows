import streamlit as st
import duckdb
import pandas as pd
import plotly.express as px

def create_dashboard():
    st.set_page_config(page_title="Weather Station Dashboard", layout="wide")
    
    st.title("Weather Station Measurements Dashboard")
    
    # Sidebar for user input
    st.sidebar.header("Filters")
    
    # Load data
    @st.cache_data
    def load_data():
        query = """
        SELECT station, min_temperature, mean_temperature, max_temperature
        FROM 'data/measurements.parquet'
        """
        return duckdb.query(query).df()

    df = load_data()
    
    # Station multiselect
    stations = sorted(df['station'].unique())
    selected_stations = st.sidebar.multiselect(
        "Select Stations",
        stations,
        default=stations[:5]  # Default to first 5 stations
    )
    
    # Filter data based on user selection
    filtered_df = df[df['station'].isin(selected_stations)]
    
    # Display summary statistics
    st.header("Summary Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average Min Temperature", f"{filtered_df['min_temperature'].mean():.2f}°C")
    col2.metric("Average Mean Temperature", f"{filtered_df['mean_temperature'].mean():.2f}°C")
    col3.metric("Average Max Temperature", f"{filtered_df['max_temperature'].mean():.2f}°C")
    
    # Create temperature distribution chart
    st.header("Temperature Distributions")
    fig = px.box(filtered_df, x='station', y=['min_temperature', 'mean_temperature', 'max_temperature'],
                 title="Temperature Distributions by Station")
    st.plotly_chart(fig, use_container_width=True)
    
    # Display the data as a table
    st.header("Raw Data")
    st.dataframe(filtered_df)

if __name__ == "__main__":
    create_dashboard()