import pandas as pd 
import os

# I point to the location of the data file, so we can access the file for the analysis.
INPUT_FILE = "data/raw/lab 1 - csv.csv"
# Here i  i want to save the processed file in the processed folder.
OUTPUT_DIR = "data/processed/"
# File name for the file that i am going to save.
SUMMARY_FILE = os.path.join(OUTPUT_DIR,"analytics_summary.csv")
TOP_PRICES_FILE = os.path.join(OUTPUT_DIR,"price_analysis.csv")
REJECTED_FILE = os.path.join(OUTPUT_DIR, "rejected_products.csv")

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

    # Calculating statistics on raw data before cleaning.
    # We need to do this now, because later we will drop the empty rows.
    count_missing_price = df['price'].isna().sum()
    count_total_products = len(df)

    #BONUS - Rejected data
    # before cleaningg, I would like to save the rows so i can look at them later.
    print("saving the rejected data")
    
    # I identified some bad data as rows where price is missing or is negative
    bad_data = df[df['price'].isna() | (df['price'] < 0)] # this will give me all the rows where price is either missing or negative.
    bad_data.to_csv(REJECTED_FILE, index=False)
    print(f"The data that was rejected is saved in {REJECTED_FILE}")

    # i can not analyise data that is missing price, so i will be deleting rows that are empty
    # Also removing negative prices, if there are any.
    df_clean = df.dropna(subset=['price'])
    df_clean = df_clean[df_clean['price'] >= 0] 
    
    print(f"amount of rows after cleaning: {len(df_clean)}")
   
   
    # Saving my results
    print("Calculating summary of the statistics")
    
    # Here i am calculating the mean 
    # Here i am calculating the mean 
    summary_data = {
        "mean_price": [df_clean['price'].mean()], # average price
        "median_price": [df_clean['price'].median()], # median price
        "total_products": [count_total_products], # total number of products before cleaning
        "missing_price_count": [count_missing_price] # number of products with missing price
    }

    

    # saving the summary data to a csv file
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_csv(SUMMARY_FILE, index=False)
    print(f"Summary is now in [{SUMMARY_FILE}]")

    # Bonus - top 10 most expensive products
    print("Calculating the top ten most expensive products")
    #I am going to be sorting the price so it is descending. To find the most expensive ones.
    top_10 = df_clean.sort_values(by="price", ascending=False).head(10)
    top_10.to_csv(TOP_PRICES_FILE, index=False)
    print(f"The top 10 most expensive list is now in {TOP_PRICES_FILE}")



if __name__ == "__main__":
    main()






    
  








    
    












    


                               
                        



