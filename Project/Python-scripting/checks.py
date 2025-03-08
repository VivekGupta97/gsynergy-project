import pandas as pd

def check_non_null(data, columns):
    for col in columns:
        if data[col].isnull().sum() > 0:
            print(f"Warning: {col} has null values")

def check_uniqueness(data, primary_key):
    if data[primary_key].duplicated().sum() > 0:
        print(f"Warning: {primary_key} has duplicates")

def check_data_types(data):
    print("Data types:\n", data.dtypes)

if __name__ == "__main__":
    fact_sales = pd.read_csv('data/fact_sales.gzip', delimiter='|')
    
    check_non_null(fact_sales, ['sku_id', 'pos_site_id'])
    check_uniqueness(fact_sales, 'transaction_id')
    check_data_types(fact_sales)
