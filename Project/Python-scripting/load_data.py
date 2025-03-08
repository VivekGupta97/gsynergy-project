import pandas as pd
import boto3  # If using AWS S3 or you can use other libraries like azure-storage-blob

def load_gzip_data_from_s3(bucket_name, file_name):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    data = pd.read_csv(obj['Body'], delimiter='|')
    return data

def load_data_to_staging(data, table_name):
    # Connect to the database (using SQLAlchemy, psycopg2, or similar)
    from sqlalchemy import create_engine
    engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
    
    # Load data to the staging table
    data.to_sql(table_name, engine, if_exists='replace', index=False)

if __name__ == "__main__":
    bucket_name = 'my-bucket'
    file_name = 'fact_sales.gzip'
    
    data = load_gzip_data_from_s3(bucket_name, file_name)
    load_data_to_staging(data, 'staging_fact_sales')
