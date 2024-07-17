import polars as pl

def create_polars_df():
    pl.Config.set_streaming_chunk_size(4000000)
    return (
        pl.scan_csv("data/measurements.txt", separator=";", has_header=False, new_columns=["station", "measure"], schema={"station": pl.String, "measure": pl.Float64})
        .group_by("station")
        .agg([
            pl.col("measure").max().alias("max"),
            pl.col("measure").min().alias("min"),
            pl.col("measure").mean().alias("mean")
        ])
        .sort("station")
        .collect(streaming=True)
    )

if __name__ == "__main__":
    import time

    start_time = time.time()
    df = create_polars_df()
    took = time.time() - start_time
    print(df)
    print(f"Polars Took: {took:.2f} sec")