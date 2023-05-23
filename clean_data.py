#Data Transformation:
#In the data_transformation/ folder, create a script called clean_data.py to clean and transform the raw data

import pandas as pd

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    
    # Data cleaning and transformation operations
    cleaned_data = df.dropna()
    
    cleaned_data.to_csv(output_file, index=False)
    
# Usage
clean_data('data/raw_data.csv', 'data/cleaned_data.csv')
