# BillionRows

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Comparison of Approaches](#comparison-of-approaches)
- [Running the Dashboard](#running-the-dashboard)

## Installation

To run this project, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/danielmschaves/bilionrows.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd your-project
   ```

3. **Create virtual environment**:

   ```bash
   poetry shell
   ```

4. **Install the required dependencies using Poetry**:

   ```bash
   poetry install
   ```

## Usage

To generate the test data file, run the following command:

```bash
make run
```

This will create a file named `measurements.txt` in the `data` directory, containing 1 billion rows of simulated weather station data.

Once the file is generated, you can run the different data processing approaches:

```bash
# Using Python's built-in functions
make python

# Using Pandas
make pandas

# Using DuckDB
make duckdb

# Using Polars
make polars
```

Each approach will read the `measurements.txt` file, process the data, and output the results.

## Comparison of Approaches

The project includes several different approaches to processing the large measurement data file:

1. **Using Python's Built-in Functions**: This approach uses Python's built-in functions and data structures to process the data. It demonstrates a straightforward way to handle the data, but may not be the most efficient for very large datasets.

2. **Using Pandas**: This approach uses the Pandas library to process the data. Pandas provides a powerful and efficient way to work with tabular data, and can take advantage of multi-core processing to speed up the computations.

3. **Using DuckDB**: DuckDB is a high-performance, in-process SQL OLAP database management system. This approach demonstrates how to use DuckDB to process the data, which can be more efficient than the Pandas approach for very large datasets.

4. **Using Polars**: Polars is a fast and efficient data manipulation library for Rust and Python. This approach shows how to use Polars to process the data, which can be even faster than the DuckDB approach for certain types of operations.

You can compare the performance of these different approaches by running the corresponding make targets and observing the execution times.

## Running the Dashboard

To run the Streamlit dashboard, use command:

1. **Run the Streamlit app**:

   ```bash
   make --always-make dashboard
   ```

This will launch the Streamlit dashboard in your default web browser.