import duckdb
import time

def create_duckdb():
    # Create the DuckDB DataFrame
    df = duckdb.sql("""
        SELECT station,
            MIN(temperature) AS min_temperature,
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperature) AS max_temperature
        FROM read_csv("data/measurements.txt", AUTO_DETECT=FALSE, sep=';', columns={'station':VARCHAR, 'temperature': 'DECIMAL(3,1)'})
        GROUP BY station
        ORDER BY station
    """)

    # Export the DataFrame to a Parquet file
    df.write_parquet("data/measurements.parquet")

    # Show the DataFrame
    df.show()

if __name__ == "__main__":
    import time
    start_time = time.time()
    create_duckdb()
    took = time.time() - start_time
    print(f"DuckDB Took: {took:.2f} sec")