import pandas as pd 
import os

# I point to the location of the data file, so we can access the file for the analysis.
INPUT_FILE = "data/raw/lab 1 - csv.csv"
# Here i  i want to save the processed file in the processed folder.
OUTPUT_DIR = "data/processed/"
SUMMORY_FILE = os.path.join(OUTPUT_DIR,"analytics_summary.csv")
TOP_PRICES_FILE = os.path.join(OUTPUT_DIR,"price_analysis.csv")

def main():
    # Reading the file
    # I first want to check if the file exists.
    if os.path.exists(INPUT_FILE):
        print(f"Error: The file {INPUT_FILE} does not exist.")
        return
    print(f"Reading the file: {INPUT_FILE}")
    

                               
                        



