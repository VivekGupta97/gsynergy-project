import pandas as pd
from sqlalchemy import create_engine

def normalize_hierarchy_data(hier_data):
    # Normalize hierarchical data
    level_1 = hier_data[['id', 'label']]
    level_2 = hier_data[['id', 'label']]  

    return level_1, level_2 

def load_normalized_data_to_db(level_1, level_2):
    engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')

    # Load normalized data into the database
    level_1.to_sql('dim_product_level_1', engine, if_exists='replace', index=False)
    level_2.to_sql('dim_product_level_2', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    hier_data = pd.read_csv('data/hier_product.gzip', delimiter='|')
    level_1, level_2 = normalize_hierarchy_data(hier_data)
    load_normalized_data_to_db(level_1, level_2)
