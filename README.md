# ETL Data Pipeline

## Overview

This project demonstrates a **simple ETL (Extract, Transform, Load) data pipeline** using Python.

The pipeline:

1. Extracts raw data from a CSV file
2. Transforms the data (cleaning and processing)
3. Loads the transformed data into a database file

This project is intended for learning and demonstration purposes.

---

## Project Structure

```
├── data.csv        # Raw input data (CSV file)
├── etl.py          # Python script that performs ETL
├── database.db     # Database storing transformed data
└── README.md       # Project documentation
```

---

## ETL Process

### Extract

* Reads raw data from a CSV file (`data.csv`)
* Uses Python to load the data into memory

### Transform

* Cleans and processes the data
* Example transformations may include:

  * Removing missing or invalid values
  * Formatting columns
  * Converting data types
  * Filtering unnecessary rows or columns

### Load

* Saves the transformed data into a database file (`database.db`)
* Data is stored in a table for easy querying and analysis

---

## Technologies Used

* Python 3
* Libraries:

  * `pandas`
  * `sqlite3`

---

## How to Run the Pipeline

1. Make sure Python is installed:

```bash
python --version
```

2. Install required libraries (if needed):

```bash
pip install pandas
```

3. Run the ETL script:

```bash
python etl.py
```

After execution:

* The raw CSV data will be transformed
* The processed data will be stored in `database.db`

---

## Output

* **Input:** `data.csv`
* **Output:** `database.db` (contains the transformed data)

---

## Use Cases

* Learning ETL fundamentals
* Preparing raw CSV data for analysis
* Simple data engineering practice project

---

## Future Improvements

* Add logging and error handling
* Validate input data schema
* Support multiple CSV files
* Add automated tests

---

## Author

**Kaushik Madhavan**
