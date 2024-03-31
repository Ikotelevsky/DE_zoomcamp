import argparse
import os
import pandas as pd
import fastparquet
from sqlalchemy import create_engine 

def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table
    url = params.url
    parquet_name = 'output.parquet'

    os.system(f'curl -o {parquet_name} {url}')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    df = pd.read_parquet(parquet_name)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    
    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')
    df.to_sql(name=table_name, con=engine, if_exists='append')              

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            description='Ingest CSV data to Postgres')
    parser.add_argument('--user', help='Username for Postgresql')
    parser.add_argument('--password', help='Password for Postgresql')
    parser.add_argument('--host', help='Host for Postgresql')
    parser.add_argument('--port', help='Port for Postgresql')
    parser.add_argument('--db', help='Database name for Postgresql')
    parser.add_argument('--table', help='Table name where we want to insert data')
    parser.add_argument('--url', help='url to the CSV')

    args = parser.parse_args()

    main(args)
