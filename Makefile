.PHONY: run

run:
	python src/create_measurements.py

python:
	python src/using_python.py

pandas:
	python src/using_pandas.py

duckdb:
	python src/using_duckdb.py
	
polars:
	python src/using_polars.py
