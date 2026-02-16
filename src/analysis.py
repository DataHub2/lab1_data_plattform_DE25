import pandas as pd 
import os

# I point to the location of the data file, so we can access the file for the analysis.
INPUT_FILE = "data/raw/lab 1 - csv.csv"
# Here i  i want to save the processed file in the processed folder.
OUTPUT_DIR = "data/processed/"
# File name for the file that i am going to save.
SUMMARY_FILE = os.path.join(OUTPUT_DIR,"analytics_summary.csv")
TOP_PRICES_FILE = os.path.join(OUTPUT_DIR,"price_analysis.csv")

def main():
    print("Starting lab")
    
    # Reading the file
    print(f"Reading file {INPUT_FILE}")

    # I checked the file and saw that it is separated by semicolons, so i implemeted the sep parameter to read the file correctly.
    df = pd.read_csv(INPUT_FILE, sep=";")
    
    print(f" Found {len(df)} rows")


    # cleaning tha data 
    # There is a risk that pandas reads the price as a string, If there is a sign that makes it look wierd. So i will manipulate the price column to make sure it is in the correct format.
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # i would also like to flag data.
    df['luxury_products'] = df['price'] > 1000 # Expensive items
    df['zero_price'] = df['price'] == 0 # item is free?
    df['missing_currency'] = df['currency'].isna() # missing currency

    # Filtering data 
    # The price can not me minus
    df = df[df['price'] >= 0]

    # i can not analyise data that is missing price, so i will be deleting rows that are empty
    #
    df_clean = df.dropna(subset=['price'])

    
    print(f"amount of rows after cleaning: {len(df_clean)}")


    # Saving my results
    
    print("Calculating summary of the statistics")
    
    # Here i am calculating the mean 
    summary_data = {
        "mean_price": [df_clean['price']. mean()], #average price
        "median_price": [df_clean['price'].median()], # median price
        "total_products": [len(df)], # the total number of products in the original data
        "missing_price_count": [df['price'].isna().sum()] # the number of products that are missing price 
    }





    
  








    
    












    


                               
                        



