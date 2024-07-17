import pandas as pd
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
import time

# Constants
CONCURRENCY = cpu_count()
TOTAL_LINES = 1_000_000_000
CHUNK_SIZE = 100_000_000
FILENAME = "data/measurements.txt"

def process_chunk(chunk):
    """Aggregate data within a chunk."""
    return chunk.groupby('station')['measure'].agg(['min', 'max', 'mean']).reset_index()

def create_aggregated_df(filename, total_lines, chunk_size=CHUNK_SIZE):
    """Create and return a DataFrame aggregated from chunks of the input file."""
    total_chunks = total_lines // chunk_size + (1 if total_lines % chunk_size else 0)
    aggregated_results = []

    try:
        with pd.read_csv(filename, sep=';', header=None, names=['station', 'measure'], chunksize=chunk_size) as reader:
            with Pool(CONCURRENCY) as pool:
                for chunk in tqdm(reader, total=total_chunks, desc="Processing"):
                    result = pool.apply_async(process_chunk, (chunk,))
                    aggregated_results.append(result)

                aggregated_results = [result.get() for result in aggregated_results]
    except Exception as e:
        print(f"Failed to process file: {e}")
        return pd.DataFrame()

    final_df = pd.concat(aggregated_results, ignore_index=True)
    return final_df.groupby('station').agg({'min': 'min', 'max': 'max', 'mean': 'mean'}).reset_index().sort_values('station')

if __name__ == "__main__":
    print("Starting file processing.")
    start_time = time.time()
    df = create_aggregated_df(FILENAME, TOTAL_LINES, CHUNK_SIZE)
    processing_time = time.time() - start_time

    print(df.head())
    print(f"Processing took: {processing_time:.2f} sec")