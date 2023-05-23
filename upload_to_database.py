#Data Storage:
#In the data_storage/ folder, create a script called upload_to_database.py to upload cleaned data to a database

import pandas as pd
import sqlalchemy

def upload_to_database(input_file, database_url, table_name):
    engine = sqlalchemy.create_engine(database_url)
    df = pd.read_csv(input_file)
    
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    
# Usage
upload_to_database('data/cleaned_data.csv', 'postgresql://user:password@localhost/mydatabase', 'finance_data')
