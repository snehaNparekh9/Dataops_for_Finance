#Data Validation and Quality:
#In the data_validation/ folder, create a script called validate_data.py to perform data validation checks

import pandas as pd

def validate_data(input_file):
    df = pd.read_csv(input_file)
    
    # Data validation checks
    if df['amount'].isnull().any():
        print("Null values found in 'amount' column.")
    if df['date'].dtype != 'datetime64[ns]':
        print("'date' column should be of type datetime.")
    # Additional validation checks...
    
# Usage
validate_data('data/cleaned_data.csv')
