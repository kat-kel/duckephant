# Duckephant

Part duck (DuckDB) and part elephant (Postgres), `duckephant` is a REST API designed to facilitate experiments and analyses of data stored in a server-based database (PostgreSQL) while leveraging the speed and efficiency of in-process databases (DuckDB).

Once you provide the information necessary to connect to the server-based, PostgreSQL database, you can access pages that let you explore and download partial or entire tables into local CSV files.

Then, if you want to continue working in SQL, you can build tables from the downloaded data files in DuckDB's in-process database system.
At which point, you can click to open a Jupyter notebook in another tab or directly execute queries using DuckDB's innovative and lightning-fast speed, designed for experimentation and analysis.

`duckephant` strives to get the beat of both worlds. On the one hand, PostgreSQL's reliable, server-baded data management system, and on the other hand, DuckDB's highly-efficient vectorized querying.

# Install

```console
$ pip install git+https://github.com/kat-kel/duckephant.git
```

# Run

```console
$ duckephant
```
