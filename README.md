# Data Engineering Lab 1 - Data Ingestion & Analysis Pipeline

This project is a part av the Programmering inom Data Platform course, the aim is to learn more about building data pipelines (ETL).

 In this case i worked on reading in raw data from a CSV-file, cleaned snd transformed the data, i also generated insights and rapports on the data.


 ## The architectur and Theory.

 To ensure the scalability and clearness of the process, this process inteds to follow the standard principles of data engineering. So that i can ensure both data quality and traceability.


 ### 1. Data Flow (Ingest → Storage → Transform → Access)
* **Ingest:** Raw data is read from `data/raw/lab 1 - csv.csv`.
* **Storage:** The script acts as the processing engine, reading from raw storage and writing to the processed layer.
* **Transform:** Data is cleaned (types normalized), validated (negative prices removed), and aggregated.
* **Access:** Final clean datasets are stored in `data/processed/`, ready for consumption.

### 2. The ETL Process
the pyhthon script `analysis.py` in `src` implements the following steps.
### Extract: 
Reads the semicolon as the separation in the CSV file using pandas.
### Transform: 
* The process:
    * Conversion of data types (strings to numerics)
    
    * Data Quality: Before i get to the cleaning, statistics on missing values are calculated to ensure accurate reporting.

    * Rejected data handling: Invalid rows (in other words-> negativ prices or missing values) are saved to another file, before i remove them from the dataset.

    * Load: Saves the cleaned summary, top 10 list, and rejected logs to the processed directory.

### 3. Technologies
* Pandas: I used Pandas for  high performance data manipulation and to analys. 
* Theoreticaly: In a production setting, libararies like Psycopg3 would load data into the postgresql database. And Pydantic would be used for data validation.

The pipeline generates three key outputs in `data/processed/`:

1.  **`analytics_summary.csv`**: Contains key metrics (Average Price, Median Price, Total Count, Missing Values Count).
2.  **`rejected_products.csv` (Bonus)**: A log of all data rows that were rejected due to quality issues (e.g., negative prices).
3.  **`price_analysis.csv` (Bonus)**: A top-10 list of the most expensive products, highlighting price deviations.

## 📂 Project Structure

```text
lab1_data_plattform/
├── data/
│   ├── raw/            # Original raw data (ReadOnly)
│   └── processed/      # Output files (Summary, Top 10, Rejected)
├── src/
│   └── analysis.py     # Main ETL script
├── pyproject.toml      # Project dependencies
└── README.md           # Documentation
















