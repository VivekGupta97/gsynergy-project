from sqlalchemy import create_engine
import pandas as pd

def load_incremental_data():
    engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')

    # Fetch the max 'last_updated' timestamp from the target table
    last_updated = pd.read_sql("SELECT MAX(last_updated) FROM fact_sales", engine)
    
    # Fetch new data from the staging table
    new_data = pd.read_sql(f"SELECT * FROM staging_fact_sales WHERE last_updated > '{last_updated}'", engine)
    
    # Insert or update the fact table
    new_data.to_sql('fact_sales', engine, if_exists='append', index=False)

if __name__ == "__main__":
    load_incremental_data()
